from fastapi import Depends, FastAPI
from fastapi.openapi.utils import get_openapi
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

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI - Inventory - python",
        version="1.0.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
