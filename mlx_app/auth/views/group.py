from mlx_model.mlx_model.tables import user, group
from mlx_model.mlx_model import session
from functools import wraps
from flask import request, Response
from settings import settings
from mlx_app.auth import token as token_validator


def is_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        given_token = request.headers['Token']
        if 'Token' in request.headers.keys():
            user = token_validator.get_user_by_valid_token(given_token)
            if user is not None:
                return f(*args, **kwargs)
            else:
                return Response("Not Found", 404)
        else:
            return Response("Missing arguments", 403)
    return decorated_function


def its_me(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        given_token = request.headers['Token']
        if 'Token' in request.headers.keys():
            user = token_validator.get_user_by_valid_token(given_token)

            if user == kwargs['id']:
                return f(*args, **kwargs)
            else:
                return Response("You don't have enough permissions", 401)
    return decorated_function