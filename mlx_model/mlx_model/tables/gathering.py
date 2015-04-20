from sqlalchemy import Column, Integer, String, ForeignKey, \
            LargeBinary, Unicode
from mlx_model.mlx_model.base import MLXBase


class GatheringType(MLXBase):
    __tablename__ = 'gathering_type'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
