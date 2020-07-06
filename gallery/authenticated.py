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