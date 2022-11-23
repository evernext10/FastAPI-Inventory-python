import asyncio
import logging
import uvicorn

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from strawberry import Schema

from configs.environment import get_environment_variables
from models.BaseModel import init
from routers.v1.ProductRouter import ProductRouter

from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.responses import PlainTextResponse
from timing_asgi import TimingMiddleware, TimingClient
from timing_asgi.integrations import StarletteScopeToName


class PrintTimings(TimingClient):
    def timing(self, metric_name, timing, tags):
        print(metric_name, timing, tags)


# Application Environment Configuration
env = get_environment_variables()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

timing = Starlette()
timing.add_middleware(
    TimingMiddleware,
    client=PrintTimings(),
    metric_namer=StarletteScopeToName(prefix="app", starlette_app=timing)
)

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION
)


static_files_app = StaticFiles(directory=".")
app.mount(path="/static", app=static_files_app, name="static")

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


if __name__ == "__main__":
    uvicorn.run(timing)