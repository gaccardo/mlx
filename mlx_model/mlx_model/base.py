from sqlalchemy.ext.declarative import declarative_base as \
    real_declarative_base

declarative_base = lambda cls: real_declarative_base(cls=cls)


@declarative_base
class MLXBase(object):
    __hide_columns__ = []

    @property
    def columns(self):
        """Return a list with the names of the entity columns."""
        return [c.name for c in self.__table__.columns]

    @property
    def columnitems(self):
        """Return dict representation of entity columns."""
        res = {}
        for column in self.columns:
            if column not in self.__hide_columns__:
                res[column] = getattr(self, column)
        return res

    def __repr__(self):
        """String representaion of the class."""
        return '{}({})'.format(self.__class__.__name__, self.columnitems)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
