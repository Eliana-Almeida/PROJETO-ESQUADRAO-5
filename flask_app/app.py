from flask import Flask, redirect
from pathlib import Path
import subprocess
import html
import sys

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent

bibliotecas = {
    "flask": {
        "nome": "Flask",
        "responsavel": "Eliana",
        "descricao": "Framework web leve para criar aplicações web com Python.",
        "arquivo": BASE_DIR / "bibliotecas/Eliana/Flask/flask_demo.py",
        "tipo": "python"
    },
    "jinja": {
        "nome": "Jinja",
        "responsavel": "Eliana",
        "descricao": "Motor de templates que conecta Python com HTML dinâmico.",
        "arquivo": BASE_DIR / "bibliotecas/Eliana/Jinja/jinja_demo.py",
        "tipo": "python"
    },
    "django": {
        "nome": "Django",
        "responsavel": "Mohamed",
        "descricao": "Framework robusto para sistemas web completos.",
        "arquivo": BASE_DIR / "bibliotecas/Mohamed/Django/django_demo.py",
        "tipo": "python"
    },
    "fastapi": {
        "nome": "FastAPI",
        "responsavel": "Mohamed",
        "descricao": "Framework moderno para criação de APIs rápidas.",
        "arquivo": BASE_DIR / "bibliotecas/Mohamed/FastAPI/fastapi_demo.py",
        "tipo": "python"
    },
    "requests": {
        "nome": "Requests",
        "responsavel": "Rafael",
        "descricao": "Biblioteca para acessar APIs e servidores web.",
        "arquivo": BASE_DIR / "bibliotecas/Rafael/Requests/requests_demo.py",
        "tipo": "streamlit"
    },
    "beautifulsoup": {
        "nome": "BeautifulSoup",
        "responsavel": "Rafael",
        "descricao": "Biblioteca para extrair dados de páginas HTML.",
        "arquivo": BASE_DIR / "bibliotecas/Rafael/BeautifulSoup/beautifulsoup_demo.py",
        "tipo": "streamlit"
    },
    "streamlit": {
        "nome": "Streamlit",
        "responsavel": "Pauliane",
        "descricao": "Cria dashboards e interfaces web interativas.",
        "arquivo": BASE_DIR / "bibliotecas/Pauliane/Streamlit/streamlit_demo.py",
        "tipo": "streamlit"
    },
    "selenium": {
        "nome": "Selenium",
        "responsavel": "Pauliane",
        "descricao": "Automatiza navegadores, cliques, testes e ações web.",
        "arquivo": BASE_DIR / "bibliotecas/Pauliane/Selenium/selenium_demo.py",
        "tipo": "python"
    },
}


def css():
    return """
    <style>
        *{box-sizing:border-box}

        body{
            margin:0;
            min-height:100vh;
            background:
                radial-gradient(circle at top, rgba(216,154,82,.28), transparent 32%),
                linear-gradient(135deg,#050816,#130d09,#050816);
            color:#f8f8f8;
            font-family:Arial, Helvetica, sans-serif;
        }

        .page{
            width:94%;
            max-width:1500px;
            margin:auto;
            padding:55px 20px;
        }

        .hero{
            text-align:center;
            margin-bottom:55px;
        }

        .hero h1{
            font-size:64px;
            letter-spacing:4px;
            color:#d89a52;
            text-shadow:0 0 28px rgba(216,154,82,.6);
            margin:0 0 20px;
        }

        .hero h2{
            color:#f4d3a0;
            font-size:28px;
            margin:0 0 18px;
        }

        .hero p{
            color:#ffffff;
            font-size:18px;
        }

        .grid{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(230px,1fr));
            gap:24px;
        }

        .card{
            background:rgba(17,24,39,.86);
            border:1px solid #b6783c;
            border-radius:18px;
            padding:24px;
            min-height:270px;
            box-shadow:0 0 22px rgba(216,154,82,.18);
        }

        .card h3{
            color:#f0b568;
            font-size:31px;
            margin:0 0 6px;
        }

        .resp{
            color:#d89a52;
            font-weight:bold;
            margin-bottom:18px;
        }

        .desc{
            color:#ffffff;
            line-height:1.5;
            min-height:58px;
        }

        .btn{
            display:block;
            width:max-content;
            min-width:130px;
            text-align:center;
            padding:11px 16px;
            margin-top:10px;
            border-radius:10px;
            text-decoration:none;
            font-weight:bold;
            color:#111;
            background:#d89a52;
        }

        .btn2{
            background:#f4d3a0;
        }

        .btn3{
            background:#ffffff;
        }

        .topbtn{
            display:inline-block;
            margin-bottom:35px;
            padding:13px 20px;
            border-radius:10px;
            background:#d89a52;
            color:#111;
            text-decoration:none;
            font-weight:bold;
        }

        .codebox{
            background:#050505;
            color:#ffffff;
            border:1px solid #b6783c;
            border-radius:16px;
            padding:28px;
            overflow:auto;
            line-height:1.65;
            font-size:15px;
            white-space:pre-wrap;
        }

        .title{
            color:#d89a52;
            font-size:54px;
            margin:10px 0;
            text-shadow:0 0 22px rgba(216,154,82,.5);
        }

        .subtitle{
            color:#ffffff;
            font-size:24px;
            margin-bottom:30px;
        }

        .note{
            background:rgba(17,24,39,.9);
            border:1px solid #b6783c;
            border-radius:14px;
            padding:20px;
            margin-bottom:25px;
            color:white;
            line-height:1.6;
        }
    </style>
    """


@app.route("/")
def home():
    cards = ""

    for slug, b in bibliotecas.items():
        cards += f"""
        <div class="card">
            <h3>{b['nome']}</h3>
            <div class="resp">{b['responsavel']}</div>
            <p class="desc">{b['descricao']}</p>

            <a class="btn" href="/codigo/{slug}">Ver código</a>
            <a class="btn btn2" href="/abrir-vscode/{slug}">Abrir no VS Code</a>
            <a class="btn btn3" href="/rodar/{slug}">Rodar ao vivo</a>
        </div>
        """

    return f"""
    <html>
    <head>
        <meta charset="UTF-8">
        {css()}
    </head>
    <body>
        <div class="page">
            <div class="hero">
                <h1>ESQUADRÃO 5</h1>
                <h2>OS ARQUITETOS WEB</h2>
                <p>Python • Web • APIs • Scraping • Automação • Dashboards</p>
            </div>

            <div class="grid">
                {cards}
            </div>
        </div>
    </body>
    </html>
    """


@app.route("/codigo/<slug>")
def codigo(slug):
    b = bibliotecas[slug]
    codigo_texto = b["arquivo"].read_text(encoding="utf-8")

    return f"""
    <html>
    <head>
        <meta charset="UTF-8">
        {css()}
    </head>
    <body>
        <div class="page">
            <a class="topbtn" href="/">← Voltar ao Portal</a>

            <h1 class="title">Código: {b['nome']}</h1>
            <h2 class="subtitle">Responsável: {b['responsavel']}</h2>

            <div class="note">
                Este é o código real da biblioteca no projeto. Ele fica no arquivo:
                <br><strong>{b['arquivo']}</strong>
            </div>

            <pre class="codebox">{html.escape(codigo_texto)}</pre>
        </div>
    </body>
    </html>
    """


@app.route("/rodar/<slug>")
def rodar(slug):
    b = bibliotecas[slug]

    if b["tipo"] == "streamlit":
        subprocess.Popen(
            ["streamlit", "run", str(b["arquivo"])],
            cwd=str(BASE_DIR),
            shell=True
        )

        return f"""
        <html>
        <head>
            <meta charset="UTF-8">
            {css()}
        </head>
        <body>
            <div class="page">
                <a class="topbtn" href="/">← Voltar ao Portal</a>

                <h1 class="title">{b['nome']} AO VIVO</h1>
                <h2 class="subtitle">Interface visual aberta pelo Streamlit</h2>

                <div class="note">
                    O Streamlit precisa abrir em uma página própria do navegador.
                    Aguarde alguns segundos e acesse:
                    <br><br>
                    <strong>http://localhost:8501</strong>
                    <br><br>
                    Esta regra vale para Streamlit, Requests e BeautifulSoup quando usam Streamlit como interface visual.
                </div>

                <a class="btn" href="http://localhost:8501" target="_blank">
                    Abrir interface Streamlit
                </a>
            </div>
        </body>
        </html>
        """

    resultado = subprocess.run(
        [sys.executable, str(b["arquivo"])],
        cwd=str(BASE_DIR),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    saida = resultado.stdout + resultado.stderr

    return f"""
    <html>
    <head>
        <meta charset="UTF-8">
        {css()}
    </head>
    <body>
        <div class="page">
            <a class="topbtn" href="/">← Voltar ao Portal</a>

            <h1 class="title">{b['nome']} AO VIVO</h1>
            <h2 class="subtitle">Resultado real executado pelo Python</h2>

            <pre class="codebox">{html.escape(saida)}</pre>
        </div>
    </body>
    </html>
    """


@app.route("/abrir-vscode/<slug>")
def abrir_vscode(slug):
    b = bibliotecas[slug]

    try:
        subprocess.Popen(["code", str(b["arquivo"])], shell=True)
    except Exception:
        pass

    return redirect(f"/codigo/{slug}")


if __name__ == "__main__":
    app.run(debug=True)