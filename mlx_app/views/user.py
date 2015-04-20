from mlx_app import app
from mlx_model.mlx_model.tables import instrument,\
    user, user_group as mlx_user_group, group as mlx_group
from mlx_model.mlx_model import session
from mlx_app.auth import token
from mlx_app.auth.views import group
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


@app.route('%s/user/<int:id>/manage' % settings.BASE_URL, 
    methods=['GET'])
@token.check_token
@group.its_me
def get_user_manage(id):
    cs = session.CreateSession()
    se = cs.get_session()

    search = se.query(
        user.User
    ).filter(
        user.User.id == id
    ).first()

    u_group = se.query(
        mlx_user_group.Group,
        mlx_group.Group
    ).filter(
        mlx_user_group.Group.user_id == id
    ).filter(
        mlx_user_group.Group.group_id == mlx_group.Group.id
    ).all()

    se.close()

    if search is not None:
        search = search.as_dict()
        search.pop('password')
        search['groups'] = list()
        for group in u_group:
            search['groups'].append(group[1].name)

        return jsonify(search)
    else:
        return jsonify({})