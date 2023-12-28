from fastapi import FastAPI, Body
from .routers import client

app = FastAPI(
    title="Vet Clinic"
)
app.include_router(client.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/hello/{name}")
async def post_hello(name: str, body=Body(None)):
    print(body)
    if type(body) != str:
        naming = body.get('data')
    else:
        naming = body
    return {"message": f"Hello {naming} from {name}"}
