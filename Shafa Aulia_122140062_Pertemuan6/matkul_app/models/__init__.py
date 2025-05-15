from sqlalchemy.orm import configure_mappers
from matkul_app.models.meta import Base
from matkul_app.models.matakuliah import Matakuliah
# from matkul_app.models.mymodel import MyModel  # jika ada

configure_mappers()

from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import register as zope_register

def get_engine(settings, prefix='sqlalchemy.'):
    return engine_from_config(settings, prefix)

def get_session_factory(engine):
    return sessionmaker(bind=engine)

def get_tm_session(session_factory, transaction_manager):
    dbsession = session_factory()
    zope_register(dbsession, transaction_manager=transaction_manager)
    return dbsession
