from engine import CreateEngine
from sqlalchemy.orm import sessionmaker, scoped_session

class CreateSession(object):

    def get_session(self):
        ce = CreateEngine()
        engine = ce.get_engine()
        session_factory = sessionmaker(bind=engine)
        return scoped_session(session_factory)


if __name__ == '__main__':
    cs = CreateSession()
    se = cs.get_session()
