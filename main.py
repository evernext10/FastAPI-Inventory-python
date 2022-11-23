from fastapi import Depends, FastAPI
from strawberry import Schema

from configs.environment import get_environment_variables
from models.BaseModel import init
from routers.v1.ProductRouter import ProductRouter

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION
)

# Add Routers
app.include_router(ProductRouter)

# Initialise Data Model Attributes
init()