from mlx_app import app
from mlx_model.mlx_model.tables import instrument,\
    user, user_group as mlx_user_group, group as mlx_group
from mlx_model.mlx_model import session
from mlx_app.auth import token
from mlx_app.auth.views import group
from settings import settings
from flask import jsonify, Response, request


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


# Instruments of the user
@app.route('%s/user/<int:id>/instruments' % settings.BASE_URL,
    methods=['GET'])
@token.check_token
def get_user_instruments(id):
    return "get user %s instruments" % id


@app.route('%s/user/<int:id>/instruments/add' % settings.BASE_URL,
    methods=['POST'])
@token.check_token
@group.its_me
def add_instrument_to_user(id):
    return "add instrument to user %s" % id


@app.route('%s/user/<int:id>/instruments/del' % settings.BASE_URL,
    methods=['POST'])
@token.check_token
@group.its_me
def del_instrument_to_user(id):
    return "del instrument to user %s" % id


# Groups of the user
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


@app.route('%s/user/<int:id>/groups' % settings.BASE_URL,
    methods=['GET'])
@token.check_token
@group.its_me
def group_of_users(id):
    cs = session.CreateSession()
    se = cs.get_session()

    u_group = se.query(
        mlx_user_group.Group,
        mlx_group.Group
    ).filter(
        mlx_user_group.Group.user_id == id
    ).filter(
        mlx_user_group.Group.group_id == mlx_group.Group.id
    ).all()

    se.close()
    result = dict()
    result['groups'] = list()
    if u_group is not None:
        for uu in u_group:
            result['groups'].append(uu[1].name)

    return jsonify(result)


@app.route('%s/user/<int:id>/groups/add' % settings.BASE_URL,
    methods=['POST'])
@token.check_token
@group.its_me
def add_group_to_user(id):
    cs = session.CreateSession()
    se = cs.get_session()
    data = request.get_json()

    search = se.query(
        mlx_user_group.Group
    ).filter(
        mlx_user_group.Group.user_id == id
    ).filter(
        mlx_user_group.Group.group_id == data['group']
    ).first()

    if search is not None:
        return Response("Group already assigned to the user", 201)

    u_group = mlx_user_group.Group(user_id=id, 
        group_id=data['group'])
    se.add(u_group)
    se.commit()
    se.close()

    return Response("Group added", 200)


@app.route('%s/user/<int:id>/groups/del' % settings.BASE_URL,
    methods=['POST'])
@token.check_token
@group.its_me
def del_group_to_user(id):
    cs = session.CreateSession()
    se = cs.get_session()
    data = request.get_json()

    search = se.query(
        mlx_user_group.Group
    ).filter(
        mlx_user_group.Group.user_id == id
    ).filter(
        mlx_user_group.Group.group_id == data['group']
    ).first()

    if search is None:
        return Response("Nothing to delete", 201)

    se.delete(search)
    se.commit()
    se.close()

    return Response("Group deleted", 200)