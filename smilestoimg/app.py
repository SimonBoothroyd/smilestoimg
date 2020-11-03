from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from smilestoimg.api.dev.api import api_router
from smilestoimg.core.config import settings

app = FastAPI(
    title="Smiles to Image", openapi_url=f"{settings.API_DEV_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_DEV_STR)
