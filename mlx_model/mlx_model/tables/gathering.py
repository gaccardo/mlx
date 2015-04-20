from sqlalchemy import Column, Integer, String, ForeignKey, \
            LargeBinary, Unicode
from mlx_model.mlx_model.base import MLXBase


class GatheringType(MLXBase):
    __tablename__ = 'gathering_type'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)



class Gathering(MLXBase):
    __tablename__ = 'gathering'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    gathering_type_id = Column(Integer, 
        ForeignKey('gathering_type.id'))
    owner_id = Column(Integer, ForeignKey('user.id'))


class UserGathering(MLXBase):
    __tablename__ = 'user_gathering'

    id = Column(Integer, primary_key=True)
    participant_id = Column(Integer, 
        ForeignKey('user.id'))
    gathering_id = Column(Integer, 
        ForeignKey('gathering.id'))