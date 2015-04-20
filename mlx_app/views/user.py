from mlx_app import app
from mlx_model.mlx_model.tables import instrument,\
    user, user_group as mlx_user_group, group as mlx_group,\
    user_instrument as mlx_user_instrument,\
    instrument as mlx_instrument, gathering
from mlx_model.mlx_model import session
from mlx_app.auth import token
from mlx_app.auth.views import group
from settings import settings
from flask import jsonify, Response, request

# User profile
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
    cs = session.CreateSession()
    se = cs.get_session()

    search = se.query(
        mlx_user_instrument.UserInstrument,
        mlx_instrument.Instrument
    ).join(
        mlx_instrument.Instrument,
        mlx_instrument.Instrument.id == \
        mlx_user_instrument.UserInstrument.instrument_id
    ).filter(
        mlx_user_instrument.UserInstrument.user_id == id
    ).all()

    result = dict()
    result['user'] = {'id': id}
    result['instruments'] = list()

    if search is not None:
        for inst in search:
            result['instruments'].append({'name':inst[1].nombre,
                                          'description':inst[1].description,
                                          'id': inst[1].id})
    return jsonify(result)


@app.route('%s/user/<int:id>/instruments/add' % settings.BASE_URL,
    methods=['POST'])
@token.check_token
@group.its_me
def add_instrument_to_user(id):
    data = request.get_json()
    cs = session.CreateSession()
    se = cs.get_session()

    if 'instrument' not in data.keys():
        return Response('Missing arguments', 403)

    search = se.query(
        mlx_user_instrument.UserInstrument
    ).filter(
        mlx_user_instrument.UserInstrument.user_id == id
    ).filter(
        mlx_user_instrument.UserInstrument.instrument_id == \
        data['instrument']
    ).first()

    if search is None:
        new_instrument2user = \
            mlx_user_instrument.UserInstrument(user_id=id, 
                                               instrument_id=data['instrument'])
        se.add(new_instrument2user)
        se.commit()
        se.close()
        return Response('Instrument added to user %d' % id, 200)
    else:
        se.close()
        return Response('Instrument already assigned to the user', 201)


@app.route('%s/user/<int:id>/instruments/del' % settings.BASE_URL,
    methods=['POST'])
@token.check_token
@group.its_me
def del_instrument_to_user(id):
    data = request.get_json()
    cs = session.CreateSession()
    se = cs.get_session()

    if 'instrument' not in data.keys():
        return Response('Missing arguments', 403)

    search = se.query(
        mlx_user_instrument.UserInstrument
    ).filter(
        mlx_user_instrument.UserInstrument.user_id == id
    ).filter(
        mlx_user_instrument.UserInstrument.instrument_id == \
        data['instrument']
    ).first()

    if search is not None:
        se.delete(search)
        se.commit()
        se.close()
        return Response('Instrument deleted from user %d' % id, 200)
    else:
        se.close()
        return Response('Nothing to delete', 201)

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


# Gatherings of the user
@app.route('%s/user/<int:id>/gatherings' % settings.BASE_URL)
@token.check_token
def get_user_gatherings(id):
    cs = session.CreateSession()
    se = cs.get_session()

    search = se.query(
        gathering.Gathering,
        gathering.GatheringType,
        user.User,
        gathering.UserGathering,
    ).join(
        gathering.GatheringType,
        gathering.Gathering.gathering_type_id == \
        gathering.GatheringType.id
    ).join(
        gathering.UserGathering,
        gathering.UserGathering.gathering_id == \
        gathering.Gathering.id
    ).join(
        user.User,
        user.User.id == gathering.UserGathering.participant_id
    ).filter(
        gathering.UserGathering.participant_id == \
        id
    ).all()

    result = dict()
    result['user'] = {'id': id}
    result['gatherings'] = list()

    for sss in search:
        result['gatherings'].append({'name': sss[0].name,
                                     'type': sss[1].name,
                                     'id': sss[0].id})

    
    return jsonify(result)


@app.route('%s/user/<int:id>/gatherings/owner' % settings.BASE_URL)
@token.check_token
def get_user_gatherings_owner(id):
    cs = session.CreateSession()
    se = cs.get_session()

    search = se.query(
        gathering.Gathering,
        gathering.GatheringType,
        user.User,
    ).join(
        gathering.GatheringType,
        gathering.Gathering.gathering_type_id == \
        gathering.GatheringType.id
    ).join(
        user.User,
        gathering.Gathering.owner_id == user.User.id
    ).filter(
        gathering.Gathering.owner_id == id
    ).all()

    result = dict()
    result['user'] = {'id': id}
    result['gatherings'] = list()

    for sss in search:
        result['gatherings'].append({'name': sss[0].name,
                                     'type': sss[1].name,
                                     'id': sss[0].id})

    return jsonify(result)


@app.route('%s/user/<int:id>/gatherings/del' % settings.BASE_URL,
    methods=['POST'])
@token.check_token
@group.its_me
def del_gathering_from_user(id):
    data = request.get_json()

    if data is None:
        return Response('Missing arguments', 403)

    if 'gathering' not in data.keys():
        return Response('Missing arguments', 403)

    cs = session.CreateSession()
    se = cs.get_session()

    search = se.query(
        gathering.UserGathering
    ).filter(
        gathering.UserGathering.participant_id == id
    ).filter(
        gathering.UserGathering.gathering_id == \
        data['gathering']
    ).first()

    if search is None:
        return Response("Nothing to delete", 201)

    se.delete(search)
    se.commit()
    se.close()

    return Response("User removed from gathering", 200)

# Invitations
@app.route('%s/user/<int:id>/invitations' % settings.BASE_URL)
@token.check_token
@group.its_me
def get_my_invitations(id):
    cs = session.CreateSession()
    se = cs.get_session()

    search = se.query(
        gathering.Invite,
        gathering.Gathering,
        gathering.GatheringType,
        user.User
    ).join(
        gathering.Gathering,
        gathering.Invite.gathering_id == \
        gathering.Gathering.id
    ).join(
        user.User,
        user.User.id == gathering.Gathering.owner_id
    ).join(
        gathering.GatheringType,
        gathering.Gathering.gathering_type_id == \
        gathering.GatheringType.id
    ).filter(
        gathering.Invite.user_id == id
    ).all()

    result = dict()
    result['invitations'] = list()

    if len(search) > 0:
        for sss in search:
            result['invitations'].append({'name': sss[1].name,
                        'type': sss[2].name,
                        'id': sss[0].id,
                        'owner': {'firstname': sss[3].firstname,
                                  'lastname': sss[3].lastname,
                                  'id': sss[3].id}})

    se.close()
    return jsonify(result)

@app.route('%s/user/<int:id>/invitations/<int:invitation_id>/accept' \
    % settings.BASE_URL)
@token.check_token
@group.its_me
def accept_invitation(id, invitation_id):
    return "accept invitation %d" % invitation_id


@app.route('%s/user/<int:id>/invitations/<int:invitation_id>/reject' \
    % settings.BASE_URL)
@token.check_token
@group.its_me
def reject_invitation(id, invitation_id):
    return "reject invitation %d" % invitation_id


@app.route('%s/user/<int:id>/invites' % settings.BASE_URL)
@token.check_token
@group.its_me
def get_my_invites(id):
    cs = session.CreateSession()
    se = cs.get_session()
    
    search = se.query(
        gathering.Invite,
        gathering.Gathering,
        gathering.GatheringType,
        user.User
    ).join(
        gathering.Gathering,
        gathering.Gathering.id == \
        gathering.Invite.gathering_id
    ).join(
        gathering.GatheringType,
        gathering.GatheringType.id == \
        gathering.Gathering.gathering_type_id
    ).join(
        user.User,
        user.User.id == \
        gathering.Invite.user_id
    ).filter(
        gathering.Gathering.owner_id == id
    ).all()

    result = dict()
    result['invites'] = list()

    if len(search) > 0:
        for sss in search:
            result['invites'].append({'name': sss[1].name,
                        'type': sss[2].name,
                        'id': sss[0].id,
                        'owner': {'firstname': sss[3].firstname,
                                  'lastname': sss[3].lastname,
                                  'id': sss[3].id}})

    se.close()
    return jsonify(result)