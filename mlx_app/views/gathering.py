from mlx_app import app
from mlx_app.auth.views import group
from mlx_model.mlx_model.tables import gathering, user
from mlx_model.mlx_model import session
from mlx_app.auth import token
from settings import settings
from flask import jsonify, Response


@app.route('%s/gatherings' % settings.BASE_URL)
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

    #import ipdb;ipdb.set_trace()

    result = dict()
    result['gatherings'] = list()

    for sss in search:
        result['gatherings'].append({'name': sss[0].name,
                    'type': sss[1].name,
                    'id': sss[0].id,
                    'owner_id': {'id': sss[2].id,
                                 'firstname': sss[2].firstname,
                                 'lastname': sss[2].lastname}})

    return jsonify(result)


@app.route('%s/gatherings/<int:id>' % settings.BASE_URL)
def get_gatherings_by_id(id):
    return "gatherings id"


@app.route('%s/gatherings/create' % settings.BASE_URL)
def create_gathering():
    return "create gathering"