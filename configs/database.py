from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from configs.environment import get_environment_variables

# Runtime Environment Configuration
env = get_environment_variables()

# Generate Database URL
#DATABASE_URL = f"{env.DATABASE_DIALECT}://{env.DATABASE_USERNAME}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOSTNAME}:{env.DATABASE_PORT}/{env.DATABASE_NAME}"
SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'

# Create Database Engine
Engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=env.DEBUG_MODE, future=True
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=Engine
)

Base = declarative_base()

def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()
