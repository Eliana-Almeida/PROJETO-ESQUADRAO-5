from pathlib import Path

BASE = Path(__file__).resolve().parent

bibliotecas = {
    "bibliotecas/Eliana/Flask": {
        "py": "flask_demo.py",
        "html": "flask.html",
        "responsavel": "Eliana",
        "nome": "Flask",
        "instalacao": "pip install flask",
        "comando": "python bibliotecas/Eliana/Flask/flask_demo.py",
        "descricao": "Flask é uma biblioteca/framework Python usada para criar páginas web e pequenos sistemas web.",
        "codigo": '''from flask import Flask

# Flask cria uma aplicação web usando Python
app = Flask(__name__)

# Esta é a rota principal da página
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Flask - Esquadrão 5</title>
        <style>
            body {
                background:#0d1117;
                color:white;
                font-family:Arial;
                text-align:center;
                padding-top:80px;
            }
            .card {
                background:#161b22;
                border:1px solid #c8874a;
                border-radius:18px;
                padding:35px;
                width:520px;
                margin:auto;
            }
            h1 { color:#c8874a; }
            p { font-size:20px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Flask funcionando ao vivo</h1>
            <p>Responsável: Eliana</p>
            <p>O Flask criou esta página web usando Python.</p>
        </div>
    </body>
    </html>
    """

# Executa a aplicação localmente na porta 5010
if __name__ == "__main__":
    app.run(port=5010, debug=True)
'''
    },

    "bibliotecas/Eliana/Jinja": {
        "py": "jinja_demo.py",
        "html": "jinja.html",
        "responsavel": "Eliana",
        "nome": "Jinja",
        "instalacao": "pip install jinja2",
        "comando": "python bibliotecas/Eliana/Jinja/jinja_demo.py",
        "descricao": "Jinja é uma biblioteca usada para criar textos e páginas HTML dinâmicas com dados vindos do Python.",
        "codigo": '''from jinja2 import Template

# Jinja permite criar um modelo com espaços para dados variáveis
template = Template("""
========================================
              JINJA AO VIVO
========================================

Responsável: {{ nome }}

Biblioteca:
{{ biblioteca }}

Função:
{{ funcao }}

Status:
{{ status }}

========================================
""")

# O Python envia os dados para dentro do modelo
resultado = template.render(
    nome="Eliana",
    biblioteca="Jinja",
    funcao="Criar conteúdo dinâmico usando Python.",
    status="Funcionando corretamente no VS Code."
)

# Mostra o resultado final no terminal
print(resultado)
'''
    },

    "bibliotecas/Mohamed/Django": {
        "py": "django_demo.py",
        "html": "django.html",
        "responsavel": "Mohamed",
        "nome": "Django",
        "instalacao": "pip install django",
        "comando": "python bibliotecas/Mohamed/Django/django_demo.py",
        "descricao": "Django é um framework Python completo para construir sistemas web maiores, com organização profissional.",
        "codigo": '''# Demonstração didática do Django
# Django é usado para sistemas web completos e robustos

print("""
========================================
              DJANGO AO VIVO
========================================

Responsável: Mohamed

O Django é um framework completo para criar sistemas web.

Ele pode trabalhar com:
- páginas web
- banco de dados
- login de usuários
- painel administrativo
- rotas
- segurança

Em um projeto real, o comando comum seria:

python manage.py runserver

Nesta demonstração, mostramos o conceito principal
do Django dentro do ecossistema dos Arquitetos Web.

Status:
Django explicado e executado com sucesso.

========================================
""")
'''
    },

    "bibliotecas/Mohamed/FastAPI": {
        "py": "fastapi_demo.py",
        "html": "fastapi.html",
        "responsavel": "Mohamed",
        "nome": "FastAPI",
        "instalacao": "pip install fastapi uvicorn",
        "comando": "python bibliotecas/Mohamed/FastAPI/fastapi_demo.py",
        "descricao": "FastAPI é um framework moderno para criar APIs rápidas, usadas na comunicação entre sistemas.",
        "codigo": '''from fastapi import FastAPI
import uvicorn

# Cria a aplicação FastAPI
app = FastAPI()

# Rota principal da API
@app.get("/")
def home():
    return {
        "grupo": "ESQUADRÃO 5",
        "tema": "OS ARQUITETOS WEB",
        "biblioteca": "FastAPI",
        "responsavel": "Mohamed",
        "status": "API funcionando ao vivo"
    }

# Rota intermediária mostrando dados do projeto
@app.get("/bibliotecas")
def bibliotecas():
    return {
        "tecnologias": ["Django", "FastAPI"],
        "funcao": "Criar sistemas web e APIs modernas"
    }

# Executa a API localmente na porta 8000
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
'''
    },

    "bibliotecas/Rafael/Requests": {
        "py": "requests_demo.py",
        "html": "requests.html",
        "responsavel": "Rafael",
        "nome": "Requests",
        "instalacao": "pip install requests",
        "comando": "python bibliotecas/Rafael/Requests/requests_demo.py",
        "descricao": "Requests é uma biblioteca Python usada para acessar sites, APIs e servidores web.",
        "codigo": '''import requests

# Requests conecta o Python com sites e APIs pela internet
print("""
========================================
              REQUESTS AO VIVO
========================================

Responsável: Rafael

A biblioteca Requests será usada para acessar uma API online.
""")

# Endereço de uma API pública
url = "https://api.github.com"

# Faz uma requisição HTTP do tipo GET
resposta = requests.get(url)

# Mostra o status da resposta
print("URL acessada:", url)
print("Status da requisição:", resposta.status_code)

# Status 200 significa sucesso
if resposta.status_code == 200:
    print("Conexão realizada com sucesso.")
else:
    print("A conexão retornou outro status.")

print("""
Explicação:
O comando requests.get(url) conecta o Python ao servidor.
O retorno 200 significa que o servidor respondeu corretamente.

========================================
""")
'''
    },

    "bibliotecas/Rafael/BeautifulSoup": {
        "py": "beautifulsoup_demo.py",
        "html": "beautifulsoup.html",
        "responsavel": "Rafael",
        "nome": "BeautifulSoup",
        "instalacao": "pip install beautifulsoup4",
        "comando": "python bibliotecas/Rafael/BeautifulSoup/beautifulsoup_demo.py",
        "descricao": "BeautifulSoup é uma biblioteca Python usada para ler HTML e extrair informações específicas de páginas web.",
        "codigo": '''from bs4 import BeautifulSoup

# HTML simulado de uma página web
html = """
<html>
    <head>
        <title>Técnico em Inteligência Artificial - Senac DF</title>
    </head>

    <body>
        <h1>Curso Técnico em Inteligência Artificial</h1>

        <p class="descricao">
            Aprenda programação, IA e automação.
        </p>
    </body>
</html>
"""

# BeautifulSoup interpreta a estrutura HTML
sopa = BeautifulSoup(html, "html.parser")

# Extrai o título principal
titulo = sopa.find("h1").text

# Extrai a descrição pela classe CSS
descricao = sopa.find("p", class_="descricao").text

print("""
========================================
          BEAUTIFULSOUP AO VIVO
========================================

Responsável: Rafael
""")

print("Título extraído:", titulo)
print("Descrição extraída:", descricao.strip())

print("""
Explicação:
O BeautifulSoup leu o HTML, encontrou as tags desejadas
e extraiu os textos da página.

========================================
""")
'''
    }
}

def criar_html(nome, responsavel, descricao, instalacao, comando, codigo):
    codigo_html = codigo.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Guia {nome} — Básico & Intermediário</title>
<style>
body {{
    background:#0d1117;
    color:#e6edf3;
    font-family:Arial, sans-serif;
    margin:0;
    line-height:1.7;
}}
header {{
    background:linear-gradient(135deg,#1f1712,#0d1117,#161b22);
    padding:45px;
    text-align:center;
    border-bottom:1px solid #30363d;
}}
h1 {{
    color:#c8874a;
    font-size:42px;
}}
.container {{
    max-width:900px;
    margin:auto;
    padding:30px;
}}
section {{
    background:#161b22;
    border:1px solid #30363d;
    border-radius:14px;
    padding:25px;
    margin:25px 0;
}}
h2 {{
    color:#e7c08a;
}}
pre {{
    background:#0d1117;
    border:1px solid #c8874a;
    border-radius:10px;
    padding:20px;
    overflow:auto;
    color:#e7c08a;
}}
code {{
    color:#e7c08a;
}}
.badge {{
    color:#c8874a;
    font-weight:bold;
}}
</style>
</head>
<body>

<header>
    <div class="badge">Python · VS Code · ESQUADRÃO 5</div>
    <h1>Guia {nome}</h1>
    <p>Básico & Intermediário — OS ARQUITETOS WEB</p>
</header>

<div class="container">

<section>
<h2>01 — O que é a biblioteca {nome}</h2>
<p>{descricao}</p>
<p><strong>Responsável:</strong> {responsavel}</p>
</section>

<section>
<h2>02 — Para que serve</h2>
<p>Esta biblioteca faz parte do ecossistema web do Python. Ela ajuda o projeto a demonstrar, na prática, como o Python pode criar, conectar, interpretar ou automatizar aplicações web.</p>
</section>

<section>
<h2>03 — Como instalar</h2>
<pre><code>{instalacao}</code></pre>
</section>

<section>
<h2>04 — Nome e caminho do arquivo</h2>
<pre><code>Arquivo: {nome.lower()}_demo.py
Comando para rodar:
{comando}</code></pre>
</section>

<section>
<h2>05 — Código didático</h2>
<pre><code>{codigo_html}</code></pre>
</section>

<section>
<h2>06 — Explicação para apresentar ao professor</h2>
<p>“Esta biblioteca foi usada para demonstrar uma função específica dentro do desenvolvimento web com Python. O código foi organizado com comentários usando # para explicar cada etapa. A execução acontece no VS Code, mostrando de forma prática como a biblioteca funciona no projeto ESQUADRÃO 5 — OS ARQUITETOS WEB.”</p>
</section>

</div>
</body>
</html>
'''

for pasta, info in bibliotecas.items():
    caminho = BASE / pasta
    caminho.mkdir(parents=True, exist_ok=True)

    (caminho / info["py"]).write_text(info["codigo"], encoding="utf-8")

    (caminho / info["html"]).write_text(
        criar_html(
            info["nome"],
            info["responsavel"],
            info["descricao"],
            info["instalacao"],
            info["comando"],
            info["codigo"]
        ),
        encoding="utf-8"
    )

    readme = f"""# {info['nome']} — {info['responsavel']}

## O que é
{info['descricao']}

## Como instalar

```bash
{info['instalacao']}