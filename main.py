import uvicorn
from fastapi import (
    FastAPI,
    Request,
)

from api import router as api_router

app = FastAPI(title="Film catalog")

app.include_router(api_router)


@app.get(path="/")
def info_page(request: Request):
    return {"message": "Hello, teapot!", "docs_page": f"{request.base_url}docs"}


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True,
    )
