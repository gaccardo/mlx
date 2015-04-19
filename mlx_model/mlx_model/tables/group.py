from sqlalchemy import Column, Integer, String, ForeignKey, \
            LargeBinary, Unicode
from mlx_model.mlx_model.base import MLXBase


class Group(MLXBase):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
