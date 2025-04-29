import uvicorn
from fastapi import (
    FastAPI,
)

from api import router as api_router

app = FastAPI(title="Film catalog")

app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True,
    )
