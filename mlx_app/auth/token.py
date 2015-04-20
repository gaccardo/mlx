from mlx_model.mlx_model.tables import token
from mlx_model.mlx_model import session
from functools import wraps
from flask import request, Response
from settings import settings

from datetime import datetime, date, time


def valid_tokens_for_user(user):
    cs = session.CreateSession()
    se = cs.get_session()

    search = se.query(
        token.Token
    ).filter(
        token.Token.user_id == user.id
    ).filter(
        token.Token.is_valid == 1
    ).first()
    se.close()

    if search is not None:
        return search.token
    
    return None

def exists_user_token(given_token):
    cs = session.CreateSession()
    se = cs.get_session()

    search = se.query(
        token.Token
    ).filter(
        token.Token.token == given_token
    ).first()
    se.close()

    if search is None:
        return False

    dt = datetime.strptime(str(search.datetime), "%Y-%m-%d %H:%M:%S.%f")
    today = datetime.now()
    diff = today - dt

    if settings.TOKEN_TTL != 0:
        if (diff.seconds / 60) > settings.TOKEN_TTL:
            return False

    if not search.is_valid:
        return False

    return True


def check_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        given_token = request.headers['Token']
        if exists_user_token(given_token):
            return f(*args, **kwargs)
        else:
            return Response('Not Authorized', 401)
    return decorated_function
