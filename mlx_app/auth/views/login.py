from mlx_app import app
from mlx_app.auth.utils import login as auth_login
from mlx_model.mlx_model.tables import user
from mlx_model.mlx_model import session
from mlx_app.auth import token
from settings import settings
from flask import jsonify, Response, request


@app.route('%s/login' % settings.BASE_URL, methods=['POST'])
def login():
    data = request.get_json()
    if 'email' in data and 'password' in data:
        aauth = auth_login.Authentication()
        user = aauth.login(data['email'], data['password'])

        if user is not None:
            return jsonify({"token":user.token})
        else:
            return Response("User or password incorrect", 401)
    else:
        return Response("Missing arguments", 403)