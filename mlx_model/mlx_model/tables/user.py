from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, \
            LargeBinary, Unicode
import sqlalchemy_utils.types as st

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    picture = Column(LargeBinary, nullable=True)
    password = Column(st.password.PasswordType(
        schemes=['md5_crypt'],
    ))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
