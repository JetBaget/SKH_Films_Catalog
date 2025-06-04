from fastapi import APIRouter, Request

from .api_v1 import router as api_v1_router

router = APIRouter(prefix="/api")

router.include_router(api_v1_router)
