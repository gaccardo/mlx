from mlx_model.mlx_model.tables import user as mlx_user, \
    token as mlx_token
from mlx_model.mlx_model import session as sss
from mlx_app.auth import token as token_validator
from passlib.hash import md5_crypt
from flask import session, Response
from functools import wraps
from datetime import datetime

import hashlib
import os

class Authentication(object):

    def generate_token(self, user):
        import ipdb;ipdb.set_trace()
        pre_token = token_validator.valid_tokens_for_user(user)
        
        if pre_token is not None:
            if token_validator.exists_user_token(pre_token):
                return pre_token

        session_creator = sss.CreateSession()
        se = session_creator.get_session()
        pre_token = hashlib.sha1(os.urandom(128)).hexdigest()
        new_token = mlx_token.Token(token=pre_token, 
                                    datetime=datetime.now(),
                                    user_id=user.id, is_valid=1)
        se.add(new_token)
        se.commit()
        se.close()

        return pre_token

    def login(self, email, password):
        session_creator = sss.CreateSession()
        se = session_creator.get_session()

        user = se.query(
                mlx_user.User
            ).filter(
                mlx_user.User.email == email,
            ).first()

        se.close()

        if user is not None:
            if md5_crypt.verify(password,
                user.password.hash):
                pre_token = self.generate_token(user)
                user.token = pre_token
                return user
            else:
                return None
        else:
            return user


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            return Response('Not Authorized', 401)
    return decorated_function