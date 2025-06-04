__all__ = ("router",)

from .list_vews import router
from .detail_vews import router as detail_router

router.include_router(detail_router)
