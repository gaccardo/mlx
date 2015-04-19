from sqlalchemy import Column, Integer, String, ForeignKey, \
            LargeBinary, Unicode
import sqlalchemy_utils.types as st
from mlx_model.mlx_model.base import MLXBase


class User(MLXBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    picture = Column(LargeBinary, nullable=True)
    password = Column(st.password.PasswordType(
        schemes=['md5_crypt'],
    ))
