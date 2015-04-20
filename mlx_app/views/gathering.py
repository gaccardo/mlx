from mlx_app import app
from mlx_app.auth.views import group
from mlx_model.mlx_model.tables import gathering, user
from mlx_model.mlx_model import session
from mlx_app.auth import token
from settings import settings
from flask import jsonify, Response, request


@app.route('%s/gatherings' % settings.BASE_URL)
@token.check_token
def get_gatherings():
    cs = session.CreateSession()
    se = cs.get_session()

    search = se.query(
        gathering.Gathering,
        gathering.GatheringType,
        user.User
    ).join(
        gathering.GatheringType,
        gathering.Gathering.gathering_type_id == \
        gathering.GatheringType.id
    ).join(
        user.User,
        gathering.Gathering.owner_id == \
        user.User.id
    ).all()

    result = dict()
    result['gatherings'] = list()

    for sss in search:
        result['gatherings'].append({'name': sss[0].name,
                    'type': sss[1].name,
                    'id': sss[0].id,
                    'owner': {'id': sss[2].id,
                                 'firstname': sss[2].firstname,
                                 'lastname': sss[2].lastname}})

    se.close()
    return jsonify(result)


@app.route('%s/gatherings/<int:id>' % settings.BASE_URL)
@token.check_token
def get_gatherings_by_id(id):
    cs = session.CreateSession()
    se = cs.get_session()

    search = se.query(
        gathering.Gathering,
        gathering.GatheringType,
        user.User
    ).join(
        gathering.GatheringType,
        gathering.Gathering.gathering_type_id == \
        gathering.GatheringType.id
    ).join(
        user.User,
        gathering.Gathering.owner_id == \
        user.User.id
    ).filter(
        gathering.Gathering.id == id
    ).first()    

    result = dict()
    result['gathering'] = dict()

    if search is None:
        return jsonify(result)

    result['gathering']['name'] = search[0].name
    result['gathering']['type'] = search[1].name
    result['gathering']['owner'] = dict()
    result['gathering']['owner']['firstname'] = search[2].firstname
    result['gathering']['owner']['lastname'] = search[2].lastname

    se.close()

    return jsonify(result)


@app.route('%s/gatherings/create' % settings.BASE_URL,
    methods=['POST'])
@token.check_token
def create_gathering():
    data = request.get_json()

    if 'name' in data.keys() and 'type' in data.keys():
        user_id = token.get_user_by_valid_token(
            request.headers.get('Token')
        )
        new_gathering = gathering.Gathering(
            name=data['name'],
            gathering_type_id=data['type'],
            owner_id=user_id
        )

        cs = session.CreateSession()
        se = cs.get_session()

        se.add(new_gathering)
        se.commit()
        se.close()

    return Response('Gathering created', 200)