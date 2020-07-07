from flask import session, redirect, url_for
from functools import wraps

def authenticated(function):
    @wraps(function)
    def authenticated_(*args, **kwargs):
        if 'username' in session:
            result = function(*args, **kwargs)
        else:
            result = redirect(url_for('login'))
        return result
    return authenticated_

def admin_authenticated(function):
    @wraps(function)
    def admin_authenticated_(*args, **kwargs):
        if 'isAdmin' in session and session['isAdmin']:
            result = function(*args, **kwargs)
        else:
            result = redirect(url_for('login'))
        return result
    return admin_authenticated_