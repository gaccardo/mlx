from mlx_app import app
from mlx_model.mlx_model.tables import instrument
from mlx_model.mlx_model import session
from settings import settings


@app.route('/mlx/api/%s/instrument' % settings.VERSION)
def get_instruments():
    cs = session.CreateSession()
    se = cs.get_session()

    search = se.query(
        instrument.Instrument
    ).all()

    import ipdb;ipdb.set_trace()

    return "instruments"
