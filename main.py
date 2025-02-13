import os
from fastapi import FastAPI, Header, HTTPException
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

app = FastAPI()

# Obtém o token do arquivo .env
auth_token = os.getenv("AUTH_TOKEN")

if auth_token is None:
    raise ValueError("A variável de ambiente AUTH_TOKEN não foi definida.")


@app.get("/")
def read_root():
    return {"message": "API está rodando!"}

@app.get("/test")
def test_token(authorization: str = Header(None)):
    if authorization != auth_token:
        raise HTTPException(status_code=401, detail="Token inválido")
    return {"message": "Token válido! Acesse a prova em https://sidebar.stract.to/api"}