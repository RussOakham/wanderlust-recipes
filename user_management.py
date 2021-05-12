""" Import functions needed for below scripts """
from flask import session

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
