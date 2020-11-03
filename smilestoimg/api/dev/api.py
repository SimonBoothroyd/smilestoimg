from fastapi import APIRouter

from smilestoimg.api.dev.endpoints import smiles

api_router = APIRouter()
api_router.include_router(smiles.router, prefix="/smiles", tags=["smiles"])
