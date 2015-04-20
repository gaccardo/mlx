from mlx_model.mlx_model.tables import user, group
from mlx_model.mlx_model import session
from functools import wraps
from flask import request, Response
from settings import settings
from mlx_app.auth import token as token_validator


def is_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        import ipdb;ipdb.set_trace()
        given_token = request.headers['Token']
        if 'Token' in request.headers.keys():
            user = token_validator.get_user_by_valid_token(given_token)
            if user is not None:
                return f(*args, **kwargs)
            else:
                Response("You don't have enough permissions", 401)
        else:
            Response("Missing arguments", 403)
    return decorated_function