from sqlalchemy import Column, Integer, String, ForeignKey, \
            LargeBinary, Unicode
from mlx_model.mlx_model.base import MLXBase
from mlx_model.mlx_model.tables import user, group


class Group(MLXBase):
    __tablename__ = 'user_group'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(user.User.id))
    group_id = Column(Integer, ForeignKey(group.Group.id))
