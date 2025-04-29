import uvicorn
from dns.resolver import query
from fastapi import (
    FastAPI,
    Request,
)


app = FastAPI(title="Film Catalog")


@app.get("/")
def hello(request: Request, name: str = "World"):
    docs_url = request.url.replace(path="docs", query="")
    return {"message": f"Hello, {name}!", "docs": str(docs_url)}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
