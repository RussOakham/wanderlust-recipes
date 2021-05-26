""" Import functions needed for below scripts """
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, abort)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from user_management import user_logged_in, log_user_in, log_user_out
from user_rating import calculate_avg_rating
if os.path.exists("env.py"):
    import env


# Flask App Configuration
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Pagination item limit
PER_PAGE = 10


# Pagination
# https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
def paginated(recipes):
    """ Sets Pagination for long content pages """
    page, per_page, offset = get_page_args(
                            page_parameter='page',
                            per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE

    return recipes[offset: offset + PER_PAGE]


def pagination_args(recipes):
    """ Sets Pagination for long content pages """
    page, per_page, offset = get_page_args(
                            page_parameter='page',
                            per_page_parameter='per_page')
    total = len(recipes)

    return Pagination(page=page, per_page=PER_PAGE, total=total)


@app.errorhandler(404)
def not_found(e):
    """ Returns custom 404 page when encountering an error """
    return render_template("404.html")


@app.route("/")
@app.route("/recipes")
def get_recipes():
    """ Returns list of recipes from database, ordered newest first """
    recipes = list(mongo.db.recipes.find().sort("created_on", -1))
    categories = mongo.db.categories.find().sort("category_title", 1)
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    return render_template(
        "recipes.html",
        recipes=recipes_paginated,
        categories=categories,
        pagination=pagination)


@app.route("/search", methods=["GET", "POST"])
def search():
    """ Build query function to submit to database find request """
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

        if "rating-search" in request.form and int(
                request.form["rating-search"]) > 0:
            min_rating = int(request.form["rating-search"])
            query["rating"] = {"$gte": min_rating}
            form_query.append({
                "key": "rating[0]",
                "value": request.form["rating-search"]
            })

    recipes = list(mongo.db.recipes.find(query).sort("created_on", -1))
    categories = mongo.db.categories.find()
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    return render_template(
        "recipes.html",
        recipes=recipes_paginated,
        categories=categories,
        pagination=pagination)


@app.route("/recipes/<recipe_title>")
def recipe(recipe_title):
    """ Returns custom recipe page for recipe with matching recipe_title """
    recipe_record = mongo.db.recipes.find_one({"url": recipe_title})

    if recipe_record:  # Valid recipe found
        # create interaction array
        interaction = {}
        if user_logged_in():
            # If user logged in, populate interaction array with historic info
            interaction = mongo.db.rating.find_one({
                "user_id": ObjectId(session['userid']),
                "recipe_id": recipe_record['_id']
            })
        # If no user historic info, populate with zero values
        if not interaction:
            interaction = {
                "rating": 0,
                "favorite": False,
            }

        return render_template(
            "recipe_detail.html",
            recipe=recipe_record,
            interaction=interaction)

    return abort(404)


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Insert new user account to database """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # Ensure Password matches Confirm Password
        if request.form.get(
             'password') != request.form.get('password-confirm'):
            flash("Passwords do not match")
            return redirect(url_for('register'))

        # Capture user information and post to database
        register_record = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "role": "user"
        }
        mongo.db.users.insert_one(register_record)

        # Log user in and add info to session cookie
        log_user_in(register_record)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Login to user account and redirect to custom profile view """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Truthy - ensure hashed password matches user input.
            if check_password_hash(
                 existing_user["password"], request.form.get("password")):
                log_user_in(existing_user)
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))

            # invalid password
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

        # username doesn't exist
        flash("Incorrect Username and/or Password")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/login/<username>", methods=["GET", "POST"])
def profile(username):
    """ Render custom profile view based upon logged in session user """
    # grab the session user's username from the db
    user = mongo.db.users.find_one(
        {"username": username}
    )

    if user:
        # If truthy

        if user['role'] == "admin":
            # If user role = admin, return all recipes
            recipes = list(mongo.db.recipes.find().sort("created_on", -1))
            # Retrieve recipes favorited by user
            favorites = list(mongo.db.rating.aggregate([
                {"$match": {"user_id": user['_id'], 'favorite': True}},
                {
                    "$lookup": {
                        "from": "recipes",
                        "localField": "recipe_id",
                        "foreignField": "_id",
                        "as": "favorites"
                    }
                },
                {"$unwind": "$favorites"},
                {"$replaceRoot": {"newRoot": "$favorites"}}
            ]))

        else:
            # Retrieve recipes from db added by user
            recipes = list(mongo.db.recipes.find(
                {"created_by": username}).sort("created_on", -1))
            # Retrieve recipes favorited by user
            favorites = list(mongo.db.rating.aggregate([
                {"$match": {"user_id": user['_id'], 'favorite': True}},
                {
                    "$lookup": {
                        "from": "recipes",
                        "localField": "recipe_id",
                        "foreignField": "_id",
                        "as": "favorites"
                    }
                },
                {"$unwind": "$favorites"},
                {"$replaceRoot": {"newRoot": "$favorites"}}
            ]))

        return render_template(
                "profile.html", username=username,
                recipes=recipes, favorites=favorites)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """ remove user from session cookies """
    if user_logged_in():
        # If truthy
        flash("You have been logged out")
        log_user_out()
        return redirect(url_for("login"))

    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """ Insert new recipe record to database """
    if user_logged_in():
        # If truthy

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
                "method_step": request.form.getlist("method_step"),
                "created_by": session["user"],
                "created_on": request.form.get("created_on"),
                "url": request.form.get(
                    "recipe_title").replace(' ', '-').lower(),
                "rating": [3, 0, 0, 0, 0, 0]
            }
            mongo.db.recipes.insert_one(new_recipe)
            flash("Recipe Submitted!")
            return redirect(url_for("get_recipes"))

        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("add_recipe.html", categories=categories)

    return redirect(url_for("login"))


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """ Update recipe record in database, by recipe_id """
    if user_logged_in():
        # If truthy

        if request.method == "POST":
            historic_rating = mongo.db.recipes.find_one(
                {"_id": ObjectId(recipe_id)})["rating"]
            update_recipe = {
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
                "method_step": request.form.getlist("method_step"),
                "created_by": session["user"],
                "created_on": request.form.get("created_on"),
                "url": request.form.get(
                    "recipe_title").replace(' ', '-').lower(),
                "rating": historic_rating
            }
            mongo.db.recipes.update(
                {"_id": ObjectId(recipe_id)}, update_recipe)
            flash("Recipe Updated!")

        recipe_record = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template(
            "edit_recipe.html", recipe=recipe_record, categories=categories)

    return redirect(url_for("login"))


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """ Remove recipe record from database, based upon recipe_id """
    if user_logged_in():
        # If truthy

        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        flash("Recipe Successfully Deleted")
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        recipes = list(mongo.db.recipes.find({"created_by": username}))
        user_id = ObjectId(session['userid'])
        favorites = list(mongo.db.rating.aggregate([
                    {"$match": {"user_id": user_id, 'favorite': True}},
                    {
                        "$lookup": {
                            "from": "recipes",
                            "localField": "recipe_id",
                            "foreignField": "_id",
                            "as": "favorites"
                        }
                    },
                    {"$unwind": "$favorites"},
                    {"$replaceRoot": {"newRoot": "$favorites"}}
                ]))
        return render_template(
                "profile.html", username=username,
                recipes=recipes, favorites=favorites)

    return redirect(url_for("login"))


@app.route("/get-categories")
def get_categories():
    """ Returns list of categories from database, ordered newest first """
    if user_logged_in():
        # If truthy

        categories = list(mongo.db.categories.find().sort("category_name", 1))
        return render_template("categories.html", categories=categories)

    return redirect(url_for("login"))


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """ Insert new category record to database """
    if user_logged_in():
        # If truthy

        if request.method == "POST":
            existing_category = mongo.db.categories.find_one(
                {"category_name": request.form.get(
                    "category_name").capitalize()})

            if existing_category:
                flash("Category Already Added")
                return redirect(url_for("get_categories"))

            category = {
                "category_name": request.form.get(
                    "category_name").capitalize(),
                "image_upload_url": request.form.get("image_upload_url"),
            }
            mongo.db.categories.insert_one(category)
            flash("New Category Added")
            return redirect(url_for("get_categories"))

        return render_template("add_category.html")

    return redirect(url_for("login"))


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """ Update category record in database, by recipe_id """
    if user_logged_in():
        # If truthy

        if request.method == "POST":
            submit = {
                "category_name": request.form.get(
                    "category_name").capitalize(),
                "image_upload_url": request.form.get("image_upload_url"),
            }
            mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
            flash("Category Updated")
            return redirect(url_for("get_categories"))

        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
        return render_template("edit_category.html", category=category)

    return redirect(url_for("login"))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """ Remove category record from database, based upon recipe_id """
    if user_logged_in():
        # If truthy

        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash("Category Successfully Deleted")
        return redirect(url_for("get_categories"))

    return redirect(url_for("login"))


@app.route("/ajax_recipe_favorite", methods=['POST'])
def ajax_recipe_favorite():
    """ Ajax request from favorite checkbox toggle to update database """
    favorite = ('favorite' in request.json)
    response = {
        "success": True,
        "flash": None,
        "response": favorite
    }

    # Check if user has already favorited recipe
    existing_interaction = mongo.db.rating.find_one({
        "user_id": ObjectId(session['userid']),
        "recipe_id": ObjectId(request.json['recipeId'])
    })

    # Update existing interaction
    if existing_interaction:
        mongo.db.rating.update_one(
            {"_id": existing_interaction['_id']}, {
                '$set': {"favorite": favorite}})

    else:
        # Create new interaction
        interaction = {
            "user_id": ObjectId(session['userid']),
            "recipe_id": ObjectId(request.json['recipeId']),
            "favorite": favorite,
            "rating": 0
        }
        mongo.db.rating.insert_one(interaction)

    return response


@app.route("/ajax_recipe_rating", methods=['POST'])
def ajax_recipe_rating():
    """
    Create AJAX request for recipe rating and updated recipe in database.
    """
    response = {
        "success": False,
        "flash": None,
        "response": -1,
    }

    # Submit 0 for rating if no rating is given.
    if 'rating' not in request.json or 'recipeId' not in request.json:
        return {"new_rating": 0}

    # Check if user has already favorited recipe
    existing_interaction = mongo.db.rating.find_one({
        "user_id": ObjectId(session['userid']),
        "recipe_id": ObjectId(request.json['recipeId'])
    })

    # Get new rating from rating submission form
    new_rating = int(request.json['rating'])

    # Format new interaction, if no historic interaction.
    old_rating = 0
    new_interaction = None
    if existing_interaction:
        new_interaction = existing_interaction['_id']
        old_rating = existing_interaction['rating']

    # Get recipe info
    recipe_detail = mongo.db.recipes.find_one(
        {"_id": ObjectId(request.json['recipeId'])})

    if not recipe_detail:
        # If no valid recipe found
        return response

    # Add new rating to 'rating' array for recipe
    # and calculate new recipe average rating (stored rating[0])
    rating = recipe_detail['rating']

    # If user already rated recipe, remove it ready for replacing.
    if old_rating > 0 and rating[old_rating] > 0:
        rating[old_rating] -= 1
    rating[new_rating] += 1
    rating[0] = calculate_avg_rating(rating)

    # Update recipe document with new average (rating[0])
    result = mongo.db.recipes.update_one(
        {"_id": ObjectId(request.json['recipeId'])},
        {
            "$set": {
                "rating.0": rating[0],
                "rating.{i}".format(i=new_rating): int(rating[new_rating]),
                "rating.{i}".format(i=old_rating): int(rating[old_rating])
            }
        })
    # If update successfull, update interaction record
    if result.matched_count > 0:
        if new_interaction is not None:
            result = mongo.db.rating.update_one(
                {"_id": new_interaction},
                {"$set": {"rating": new_rating}}
            )
        # If no record found creates new record with additional info
        else:
            result = mongo.db.rating.insert_one({
                "user_id": ObjectId(session['userid']),
                "recipe_id": ObjectId(request.json['recipeId']),
                "favorite": False,
                "rating": new_rating
            })

        response["success"] = True

    response["response"] = new_rating
    return response


@app.route("/ajax_user_comment", methods=['POST'])
def ajax_user_comment():
    """
    Create AJAX request for user comment
    and append to array in recipe database.
    """
    response = {
        "success": False,
        "flash": None,
        "response": None
    }
    if "comment" in request.json and len(request.json["comment"]) > 0:
        comment = {
            "author": session["user"].capitalize(),
            "text": request.json['comment']
        }
        mongo.db.recipes.update_one(
            {"_id": ObjectId(request.json['recipeId'])},
            {"$push": {"comments": comment}}
            )
        response["success"] = True
        response["response"] = comment

    return response


@app.route("/delete_user_comment", methods=['POST'])
def ajax_delete_comment():
    """
    Create AJAX request to delete user comment
    and remove from array in recipe database.
    """
    response = {
        "success": False,
        "flash": None,
        "response": None
    }
    if "comment" in request.json and "recipe" in request.json:
        index = int(request.json["comment"])
        mongo.db.recipes.update(
            {"_id": ObjectId(request.json['recipe'])},
            {"$unset": {"comments.{i}".format(i=index): None}}
        )
        mongo.db.recipes.update(
            {"_id": ObjectId(request.json['recipe'])},
            {"$pull": {"comments": None}}
        )

    return response


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
