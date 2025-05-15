from setuptools import setup, find_packages

setup(
    name='matkul_app',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyramid',
        'SQLAlchemy',
        'alembic',
        'pyramid_tm',
        'pyramid_retry',
        'zope.sqlalchemy',
        'waitress',
    ],
    entry_points={
        'paste.app_factory': [
            'main = matkul_app:main',
        ],
    },
)