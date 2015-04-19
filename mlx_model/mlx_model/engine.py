from sqlalchemy import create_engine
from settings import settings

class CreateEngine(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CreateEngine, cls).__new__(
                cls, *args, **kwargs
            )

        return cls._instance

    def __init__(self):
        self.engine = None

    def get_engine(self):
        if self.engine is None:
            self.engine = create_engine(settings.DB_URL)

        return self.engine


if __name__ == '__main__':
    ce = CreateEngine()
    en = ce.get_engine()

    import ipdb;ipdb.set_trace()
