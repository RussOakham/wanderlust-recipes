import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "recipes.html", recipes=recipes, categories=categories)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = {}
    form_query = []

    if request.method == "POST":
        # Construct the search query with {key: value}
        if "search-text" in request.form and request.form["search-text"]:
            query["$text"] = {
                "$search": request.form["search-text"],
                "$caseSensitive": False,
            }
            form_query.append({
                "key": "search-text",
                "value": request.form["search-text"]
            })

        if "category_name" in request.form and request.form["category_name"]:
            query["category_name"] = request.form["category_name"]
            form_query.append({
                "key": "category_name",
                "value": request.form["category_name"]
            })

        if "servings" in request.form and request.form["servings"]:
            query["servings"] = request.form["servings"]
            form_query.append({
                "key": "servings",
                "value": request.form["servings"]
            })

    recipes = mongo.db.recipes.find(query)
    categories = mongo.db.categories.find()
    return render_template("recipes.html", recipes=recipes, categories=categories)


@app.route("/recipes/<recipe_title>")
def recipe(recipe_title):
    recipe = mongo.db.recipes.find_one({"url": recipe_title})
    return render_template("recipe_detail.html", recipe=recipe)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Truthy - ensure hased password matches user input.
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/login/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        # If truthy
        # Retrieve recipes from db added by user
        recipes = list(mongo.db.recipes.find({"created_by": username}))
        return render_template(
            "profile.html", username=username, recipes=recipes)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        new_recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_title": request.form.get("recipe_title"),
            "image_upload_url": request.form.get("image_upload_url"),
            "servings": request.form.get("servings"),
            "prep_hours": request.form.get("prep_hours"),
            "prep_minutes": request.form.get("prep_minutes"),
            "cook_hours": request.form.get("cook_hours"),
            "cook_minutes": request.form.get("cook_minutes"),
            "recipe_description": request.form.get("recipe_description"),
            "ingredients": request.form.getlist("ingredients"),
            "method-step": request.form.getlist("method-step"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(new_recipe)
        flash("Recipe Submitted!")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_recipe.html", recipe=recipe, categories=categories)


@app.route("/get-categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name").capitalize()
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name").capitalize()
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
