from pathlib import Path

BASE = Path(__file__).resolve().parent

dados = {
    "bibliotecas/Eliana/Flask": {
        "py": "flask_demo.py",
        "html": "flask.html",
        "responsavel": "Eliana",
        "biblioteca": "Flask",
        "descricao": "Framework web leve para criar aplicações e páginas web com Python.",
        "run": "python bibliotecas/Eliana/Flask/flask_demo.py",
        "codigo": '''from flask import Flask

# Importa o Flask, biblioteca usada para criar aplicações web com Python
app = Flask(__name__)

# Rota principal da página
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Flask ao Vivo</title>
        <style>
            body {
                background:#0d1117;
                color:white;
                font-family:Arial;
                text-align:center;
                padding-top:100px;
            }
            h1 {
                color:#c8874a;
                font-size:60px;
            }
            p {
                font-size:24px;
            }
        </style>
    </head>
    <body>
        <h1>FLASK AO VIVO</h1>
        <p>Biblioteca apresentada por Eliana</p>
        <p>Flask criando uma página web real com Python.</p>
    </body>
    </html>
    """

# Executa o servidor Flask na porta 5010
if __name__ == "__main__":
    app.run(port=5010, debug=True)
'''
    },
    "bibliotecas/Eliana/Jinja": {
        "py": "jinja_demo.py",
        "html": "jinja.html",
        "responsavel": "Eliana",
        "biblioteca": "Jinja",
        "descricao": "Motor de templates que conecta Python com HTML dinâmico.",
        "run": "python bibliotecas/Eliana/Jinja/jinja_demo.py",
        "codigo": '''from jinja2 import Template

# Jinja permite criar textos ou páginas HTML usando variáveis do Python
template = Template("""
========================================
             JINJA AO VIVO
========================================

Responsável: {{ nome }}

Função:
{{ funcao }}

Status:
{{ status }}

========================================
""")

# Aqui o Python envia dados para dentro do template
resultado = template.render(
    nome="Eliana",
    funcao="Gerar HTML dinâmico com Python.",
    status="Jinja funcionando perfeitamente!"
)

# Exibe o resultado no terminal
print(resultado)
'''
    },
    "bibliotecas/Mohamed/Django": {
        "py": "django_demo.py",
        "html": "django.html",
        "responsavel": "Mohamed",
        "biblioteca": "Django",
        "descricao": "Framework completo para desenvolvimento web robusto.",
        "run": "python bibliotecas/Mohamed/Django/django_demo.py",
        "codigo": '''# Django é um framework web completo para criação de sistemas profissionais
# Este exemplo demonstra o conceito de estrutura web robusta no terminal

print("""
========================================
             DJANGO AO VIVO
========================================

Responsável: Mohamed

Django é usado para criar sistemas web completos,
com rotas, banco de dados, autenticação, painel admin
e arquitetura profissional.

Exemplo básico:
- Criar projeto
- Criar app
- Criar views
- Criar urls
- Rodar servidor

Comando real em projetos Django:
python manage.py runserver

Status:
Django demonstrado com sucesso!

========================================
""")
'''
    },
    "bibliotecas/Mohamed/FastAPI": {
        "py": "fastapi_demo.py",
        "html": "fastapi.html",
        "responsavel": "Mohamed",
        "biblioteca": "FastAPI",
        "descricao": "Framework moderno para criação de APIs rápidas com Python.",
        "run": "python bibliotecas/Mohamed/FastAPI/fastapi_demo.py",
        "codigo": '''from fastapi import FastAPI
import uvicorn

# Cria a aplicação FastAPI
app = FastAPI()

# Rota principal da API
@app.get("/")
def home():
    return {
        "projeto": "ESQUADRÃO 5",
        "biblioteca": "FastAPI",
        "responsavel": "Mohamed",
        "status": "API funcionando ao vivo"
    }

# Rota intermediária simulando dados de bibliotecas web
@app.get("/bibliotecas")
def listar_bibliotecas():
    return {
        "bibliotecas": ["Django", "FastAPI"],
        "uso": "Criação de APIs e sistemas web modernos"
    }

# Executa a API na porta 8000
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
'''
    },
    "bibliotecas/Rafael/Requests": {
        "py": "requests_demo.py",
        "html": "requests.html",
        "responsavel": "Rafael",
        "biblioteca": "Requests",
        "descricao": "Biblioteca para acessar sites, APIs e servidores web.",
        "run": "python bibliotecas/Rafael/Requests/requests_demo.py",
        "codigo": '''import requests

# Requests permite conectar o Python com sites e APIs pela internet
print("""
========================================
             REQUESTS AO VIVO
========================================

Responsável: Rafael

Conectando com uma API online...
""")

# URL pública usada para teste
url = "https://api.github.com"

# Faz uma requisição GET
resposta = requests.get(url)

# Mostra o status da conexão
print("Status:", resposta.status_code)

# Mostra confirmação
if resposta.status_code == 200:
    print("Conexão realizada com sucesso!")
else:
    print("A conexão retornou outro status.")

print("""
========================================
""")
'''
    },
    "bibliotecas/Rafael/BeautifulSoup": {
        "py": "beautifulsoup_demo.py",
        "html": "beautifulsoup.html",
        "responsavel": "Rafael",
        "biblioteca": "BeautifulSoup",
        "descricao": "Biblioteca para extrair dados de páginas HTML.",
        "run": "python bibliotecas/Rafael/BeautifulSoup/beautifulsoup_demo.py",
        "codigo": '''from bs4 import BeautifulSoup

# BeautifulSoup é usado para ler e extrair informações de páginas HTML
html = """
<html>
<head>
    <title>Esquadrão 5</title>
</head>
<body>
    <h1>BeautifulSoup ao vivo</h1>
    <p>Extraindo dados de uma página HTML.</p>
</body>
</html>
"""

# Lê o HTML com o BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

print("""
========================================
          BEAUTIFULSOUP AO VIVO
========================================

Responsável: Rafael
""")

# Extrai dados específicos do HTML
print("Título:", soup.title.text)
print("H1:", soup.h1.text)
print("Parágrafo:", soup.p.text)

print("""
========================================
""")
'''
    },
}

def html_page(nome, responsavel, descricao, codigo, run):
    safe = codigo.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
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
    line-height:1.7;
    margin:0;
}}
header {{
    background:linear-gradient(135deg,#1f1712,#0d1117,#161b22);
    padding:45px;
    text-align:center;
    border-bottom:1px solid #30363d;
}}
h1 {{
    color:#c8874a;
    font-size:46px;
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
.num {{
    color:#c8874a;
    font-weight:bold;
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
</style>
</head>
<body>
<header>
    <h1>Guia {nome}</h1>
    <p>Básico & Intermediário — Python · VS Code · Web</p>
</header>

<div class="container">

<section>
    <h2><span class="num">01</span> O que é {nome}</h2>
    <p>{descricao}</p>
    <p><strong>Responsável:</strong> {responsavel}</p>
</section>

<section>
    <h2><span class="num">02</span> Instalação e execução no VS Code</h2>
    <pre><code># Instalar dependências quando necessário
pip install flask jinja2 django fastapi uvicorn requests beautifulsoup4

# Rodar esta biblioteca
{run}</code></pre>
</section>

<section>
    <h2><span class="num">03</span> Código básico e intermediário</h2>
    <pre><code>{safe}</code></pre>
</section>

<section>
    <h2><span class="num">04</span> O que demonstrar ao professor</h2>
    <p>Mostrar o arquivo no VS Code, explicar os comentários com <code>#</code>, executar no terminal e provar o funcionamento real do código.</p>
</section>

</div>
</body>
</html>'''

for pasta, info in dados.items():
    path = BASE / pasta
    path.mkdir(parents=True, exist_ok=True)

    (path / info["py"]).write_text(info["codigo"], encoding="utf-8")

    (path / info["html"]).write_text(
        html_page(
            info["biblioteca"],
            info["responsavel"],
            info["descricao"],
            info["codigo"],
            info["run"]
        ),
        encoding="utf-8"
    )

    readme = f"""# {info['biblioteca']} — {info['responsavel']}

## Função da biblioteca
{info['descricao']}

## Como rodar no VS Code

```bash
{info['run']}