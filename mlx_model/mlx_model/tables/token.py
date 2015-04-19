from sqlalchemy import Column, Integer, String, ForeignKey, \
            LargeBinary, Unicode, DateTime, text
import sqlalchemy_utils.types as st
from mlx_model.mlx_model.base import MLXBase
from mlx_model.mlx_model.tables import user


class User(MLXBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    token = Column(String(50), nullable=False)
    datetime = Column(DateTime, server_default=text('now()'))
    user = Column(Integer, ForeignKey(user.User.id))
