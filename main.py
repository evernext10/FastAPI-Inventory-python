from fastapi import Depends, FastAPI
from strawberry import Schema

from configs.environment import get_environment_variables


# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION
)