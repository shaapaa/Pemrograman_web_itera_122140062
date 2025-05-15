from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from sqlalchemy import engine_from_config
from .models.meta import Base

def main(global_config, **settings):
    # Session factory
    session_factory = SignedCookieSessionFactory(settings['session.secret'])
    config = Configurator(settings=settings, session_factory=session_factory)

    # Enable Jinja2 for HTML rendering
    config.include('pyramid_jinja2')

    # Database setup
    engine = engine_from_config(settings, 'sqlalchemy.')
    Base.metadata.bind = engine

    # Middlewares & debug
    config.include('pyramid_tm')
    config.include('pyramid_retry')
    config.include('pyramid_debugtoolbar')

    # Static assets
    config.add_static_view('static', 'matkul_app:static', cache_max_age=3600)

    # Routes and views
    config.include('.routes')
    config.scan('.views')

    return config.make_wsgi_app()
