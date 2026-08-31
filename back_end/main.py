from fastapi import FastAPI, Response, Request, Header
from back_end.proto.package import User

app = FastAPI()

users_db: dict[str, User] = {}

@app.get("/show-informations")
def show_informations(forms_client_token: str = Header(..., description="Token único do cliente")):
    if forms_client_token not in users_db:
        users_db[forms_client_token] = User()
    
    user = users_db[forms_client_token]
    
    return Response(
        content=bytes(user),
        status_code=200
    )

@app.post("/update-informations")
async def update_informations(request: Request, forms_client_token: str = Header(..., description="Token único do cliente")):
    raw_body = await request.body()
    
    if forms_client_token not in users_db:
        users_db[forms_client_token] = User()
    
    users_db[forms_client_token].parse(raw_body)
    
    return Response(status_code=200)

@app.get("/all-users-db")
def all_users_db():
    return users_db
    