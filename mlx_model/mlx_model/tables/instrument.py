from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, \
        LargeBinary, Unicode


Base = declarative_base()


class Instrument(Base):
    __tablename__ = 'instrument'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    description = Column(Unicode)
    picture = Column(LargeBinary, nullable=True)
