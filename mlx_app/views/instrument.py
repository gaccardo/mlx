from mlx_app import app
from mlx_model.mlx_model.tables import instrument
from mlx_model.mlx_model import session
from settings import settings
from flask import jsonify


@app.route('/mlx/api/%s/instrument' % settings.VERSION)
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

    return jsonify(instruments)
