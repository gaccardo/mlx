from sqlalchemy.ext.declarative import declarative_base as \
    real_declarative_base

declarative_base = lambda cls: real_declarative_base(cls=cls)


@declarative_base
class MLXBase(object):

    def __repr__(self):
        """String representaion of the class."""
        return '{}({})'.format(self.__class__.__name__, self.columnitems)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
