import os, sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Load config and logging
config = context.config
fileConfig(config.config_file_name)
print("=== SQLAlchemy URL dari Alembic ===")
print(config.get_main_option("sqlalchemy.url"))

# Make sure app package is on PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your model’s Base and metadata
from matkul_app.models.meta import Base
from matkul_app.models.matakuliah import Matakuliah

target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata,
        literal_binds=True, dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    # Ambil url database dari config
    url = config.get_main_option("sqlalchemy.url")

    # Buat dictionary konfigurasi minimal yang hanya berisi url database
    connectable = engine_from_config(
        {"sqlalchemy.url": url},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
