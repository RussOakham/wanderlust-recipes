""" Import functions needed for below scripts """
from flask import session, flash, redirect, url_for
from functools import wraps


def user_logged_in():
    """ Returns if user is currently logged in """
    if session.get("user") is None:
        return False

    return True


def log_user_in(username):
    """ Adds user info to session cookie """
    session['user'] = username['username']
    session['userid'] = str(username['_id'])
    session['userrole'] = username['role']


def log_user_out():
    """ Removes the current user from the session cookie """
    session.pop('user')
    session.pop('userid')
    session.pop('userrole')


def requires_logged_in_user(func):
    """ Disables a wrapped route if user is not logged in """
    @wraps(func)
    def route(*args, **kwargs):
        if user_logged_in():
            # If a user is logged in proceed with function
            return func(*args, **kwargs)

        # If user is not logged in, redirect to login page with error message
        flash("You need to be logged in to access that page!",
              category="error")
        return redirect(url_for("login"))

    return route


def requires_user_not_logged_in(func):
    """ Disables a wrapped route if a user is logged in """
    @wraps(func)
    def route(*args, **kwargs):
        if not user_logged_in():
            # If no user logged in, call the function
            return func(*args, **kwargs)

        # If user is logged in, redirect to home with error message
        flash("User logged in!", category="error")
        return redirect(url_for("get_recipes"))

    return route
