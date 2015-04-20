from sqlalchemy import Column, Integer, String, ForeignKey, \
            LargeBinary, Unicode
from mlx_model.mlx_model.base import MLXBase
from mlx_model.mlx_model.tables import user, instrument


class UserInstrument(MLXBase):
    __tablename__ = 'user_instrument'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(user.User.id))
    instrument_id = Column(Integer, 
        ForeignKey(instrument.Instrument.id))
