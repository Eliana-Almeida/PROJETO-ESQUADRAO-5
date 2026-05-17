from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import uvicorn

# =========================================================
# FASTAPI - ESQUADRAO 5
# OS ARQUITETOS WEB
# Responsavel: Mohamed
# =========================================================

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return pagina()

@app.post("/", response_class=HTMLResponse)
def processar(
    nome: str = Form(...),
    area: str = Form(...),
    tecnologia: str = Form(...)
):
    resultado = f"""
    <div class="resultado">
        <h2>Resposta criada pela API</h2>
        <p><strong>Nome:</strong> {nome}</p>
        <p><strong>Área:</strong> {area}</p>
        <p><strong>Tecnologia:</strong> {tecnologia}</p>
        <p>A FastAPI recebeu os dados, processou a requisição POST e devolveu esta resposta HTML.</p>
    </div>
    """
    return pagina(nome, area, tecnologia, resultado)

@app.get("/api", response_class=HTMLResponse)
def api_visual():
    return """
    <html>
    <head><meta charset="UTF-8"></head>
    <body style="background:#050816;color:white;font-family:Arial;padding:40px;">
        <h1 style="color:#d89a52;">FASTAPI JSON</h1>
        <pre style="background:black;padding:25px;border-radius:15px;">
{
    "projeto": "ESQUADRAO 5",
    "tema": "OS ARQUITETOS WEB",
    "biblioteca": "FastAPI",
    "status": "API funcionando"
}
        </pre>
    </body>
    </html>
    """

def pagina(nome="", area="Desenvolvimento Web", tecnologia="FastAPI", resultado=""):
    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
    <meta charset="UTF-8">
    <title>FastAPI ao Vivo</title>

    <style>
    body {{
        background: radial-gradient(circle at top, #2a180d, #050816 45%);
        color: white;
        font-family: Arial;
        margin: 0;
        padding: 50px;
    }}

    .voltar {{
        display: inline-block;
        background: #d89a52;
        color: #111;
        border: none;
        padding: 12px 18px;
        border-radius: 10px;
        font-weight: bold;
        cursor: pointer;
        margin-bottom: 25px;
        text-decoration: none;
    }}

    .container {{
        max-width: 760px;
        margin: auto;
        background: #161b22;
        border: 1px solid #d89a52;
        border-radius: 22px;
        padding: 38px;
        box-shadow: 0 0 35px rgba(216,154,82,0.35);
    }}

    h1 {{
        color: #d89a52;
        text-align: center;
        font-size: 42px;
    }}

    p {{
        line-height: 1.6;
    }}

    label {{
        display: block;
        margin-top: 18px;
        color: #f4d3a0;
        font-weight: bold;
    }}

    input, select {{
        width: 100%;
        padding: 14px;
        margin-top: 8px;
        border-radius: 10px;
        border: 1px solid #30363d;
        background: #0d1117;
        color: white;
        font-size: 16px;
    }}

    button {{
        margin-top: 25px;
        width: 100%;
        padding: 15px;
        border: none;
        border-radius: 12px;
        background: #d89a52;
        color: #111;
        font-weight: bold;
        font-size: 18px;
        cursor: pointer;
    }}

    .resultado {{
        margin-top: 30px;
        padding: 22px;
        border-radius: 14px;
        background: #0d1117;
        border: 1px solid #3dd68c;
    }}

    .resultado h2 {{
        color: #3dd68c;
    }}

    .api {{
        display: inline-block;
        margin-top: 20px;
        color: #d89a52;
        font-weight: bold;
    }}
    </style>
    </head>

    <body>

    <a class="voltar" href="http://127.0.0.1:5000">← Voltar ao Portal</a>

    <div class="container">
        <h1>FASTAPI AO VIVO</h1>

        <p>
            Esta página mostra a FastAPI funcionando na prática:
            rota GET, rota POST, formulário, processamento e resposta.
        </p>

        <form method="POST">
            <label>Nome</label>
            <input type="text" name="nome" placeholder="Digite o nome do apresentador" value="{nome}" required>

            <label>Área</label>
            <select name="area">
                <option>Desenvolvimento Web</option>
                <option>APIs e Sistemas Digitais</option>
                <option>Inteligencia Artificial</option>
                <option>Automacao Web</option>
            </select>

            <label>Tecnologia</label>
            <input type="text" name="tecnologia" value="{tecnologia}" required>

            <button type="submit">Enviar para a FastAPI</button>
        </form>

        <a class="api" href="/api" target="_blank">Ver exemplo de resposta JSON da API</a>

        {resultado}
    </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5013)