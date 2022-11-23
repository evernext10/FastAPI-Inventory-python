from fastapi import Depends, FastAPI
from strawberry import Schema

from configs.environment import get_environment_variables
from models.BaseModel import init

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION
)

# Initialise Data Model Attributes
init()