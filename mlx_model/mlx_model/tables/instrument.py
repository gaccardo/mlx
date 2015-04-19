from sqlalchemy import Column, Integer, String, ForeignKey, \
        LargeBinary, Unicode
from mlx_model.mlx_model.base import MLXBase


class Instrument(MLXBase):
    __tablename__ = 'instrument'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    description = Column(Unicode)
    picture = Column(LargeBinary, nullable=True)
