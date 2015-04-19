from mlx_app import app
from mlx_model.mlx_model.tables import instrument
from mlx_model.mlx_model import session
from settings import settings
from flask import jsonify, Response

@app.route('%s/instrument' % settings.BASE_URL)
def get_instruments():
    cs = session.CreateSession()
    se = cs.get_session()

    search = se.query(
        instrument.Instrument
    ).all()

    instruments = dict()
    instruments['instruments'] = list()
    for inst in search:
        instruments['instruments'].append(inst.as_dict())

    se.close()
    return jsonify(instruments)


@app.route('%s/instrument/<int:id>' % settings.BASE_URL)
def get_instrument(id):
    cs = session.CreateSession()
    se = cs.get_session()

    search = se.query(
        instrument.Instrument
    ).filter(
        instrument.Instrument.id == id
    ).first()

    se.close()
    if search is None:
        return Response('Not Found', 404)
    return jsonify(search.as_dict())
