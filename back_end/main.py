from fastapi import FastAPI, Response, Request
from back_end.proto.package import User

app = FastAPI()

user = User()

@app.get("/show-informations")
def show_informations():
    return Response(
        content=bytes(user),
        status_code=200
    )

@app.post("/update-informations")
async def update_informations(request: Request):
    global user
    # Lê os bytes brutos enviados pelo front
    raw_body = await request.body()

    # Desserializa para o proto
    user.parse(raw_body)

    return Response(status_code=200)