from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "ESQUADRÃO 5: OS ARQUITETOS WEB"}

@app.get("/api")
def api():
    return {"mensagem": "API funcionando com FastAPI"}