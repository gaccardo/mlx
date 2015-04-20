from sqlalchemy import Column, Integer, String, ForeignKey, \
            LargeBinary, Unicode, TIMESTAMP
import sqlalchemy_utils.types as st
from mlx_model.mlx_model.base import MLXBase
from mlx_model.mlx_model.tables import user


class Token(MLXBase):
    __tablename__ = 'token'

    id = Column(Integer, primary_key=True)
    token = Column(String(50), nullable=False)
    datetime = Column(TIMESTAMP)
    user_id = Column(Integer, ForeignKey(user.User.id))
