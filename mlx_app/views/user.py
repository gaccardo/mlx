from mlx_app import app
from mlx_model.mlx_model.tables import instrument, user
from mlx_model.mlx_model import session
from mlx_app.auth import token
from settings import settings
from flask import jsonify, Response


@app.route('%s/user/<int:id>' % settings.BASE_URL)
@token.check_token
def get_user(id):
    cs = session.CreateSession()
    se = cs.get_session()

    search = se.query(
        user.User
    ).filter(
        user.User.id == id
    ).first()

    se.close()

    if search is not None:
        search = search.as_dict()
        search.pop('password')
        return jsonify(search)
    else:
        return jsonify({})
