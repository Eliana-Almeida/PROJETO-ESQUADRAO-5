from flask import Flask, render_template_string, request
from bs4 import BeautifulSoup

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>BeautifulSoup ao Vivo</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            font-family: Arial, Helvetica, sans-serif;
            background:
                radial-gradient(circle at center, rgba(220, 150, 70, 0.22), transparent 35%),
                #050815;
            color: #f4f4f4;
        }

        .voltar {
            position: fixed;
            top: 35px;
            left: 32px;
            background: #e0a050;
            color: #111;
            text-decoration: none;
            padding: 12px 20px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 14px;
            box-shadow: 0 0 18px rgba(224, 160, 80, 0.45);
        }

        .voltar:hover {
            background: #f0b765;
        }

        .container {
            width: 92%;
            max-width: 720px;
            margin: 80px auto 40px;
            background: #171c23;
            border: 1px solid #d99545;
            border-radius: 16px;
            padding: 42px 34px;
            box-shadow: 0 0 35px rgba(217, 149, 69, 0.45);
        }

        h1 {
            text-align: center;
            color: #e09a42;
            font-size: 36px;
            margin-bottom: 25px;
            text-transform: uppercase;
        }

        p {
            font-size: 15px;
            line-height: 1.7;
            color: #e8e8e8;
        }

        label {
            display: block;
            margin-top: 18px;
            margin-bottom: 8px;
            color: #e6c28c;
            font-weight: bold;
        }

        textarea, select {
            width: 100%;
            padding: 13px;
            border-radius: 8px;
            border: 1px solid #303744;
            background: #080c14;
            color: #fff;
            font-weight: bold;
            outline: none;
        }

        textarea {
            min-height: 130px;
            resize: vertical;
        }

        textarea:focus, select:focus {
            border-color: #e09a42;
            box-shadow: 0 0 10px rgba(224, 154, 66, 0.35);
        }

        button {
            width: 100%;
            margin-top: 22px;
            padding: 14px;
            border: none;
            border-radius: 9px;
            background: #e0a050;
            color: #111;
            font-weight: bold;
            font-size: 15px;
            cursor: pointer;
        }

        button:hover {
            background: #f0b765;
        }

        .link-api {
            display: inline-block;
            margin-top: 18px;
            color: #e0a050;
            font-weight: bold;
            font-size: 14px;
        }

        .resposta {
            margin-top: 28px;
            border: 1px solid #27b36a;
            border-radius: 12px;
            padding: 25px 22px;
            background: #0d1118;
        }

        .resposta h2 {
            color: #2ecc71;
            margin-top: 0;
        }

        .resposta p {
            font-size: 14px;
            font-weight: bold;
        }

        .item {
            color: #2ecc71;
        }

        @media (max-width: 700px) {
            .voltar {
                position: static;
                display: inline-block;
                margin: 20px;
            }

            .container {
                margin-top: 20px;
                padding: 30px 22px;
            }

            h1 {
                font-size: 28px;
            }
        }
    </style>
</head>
<body>

    <a href="/" class="voltar">← Voltar ao Portal</a>

    <main class="container">
        <h1>BeautifulSoup ao Vivo</h1>

        <p>
            Esta página mostra a biblioteca BeautifulSoup funcionando na prática:
            ela recebe um código HTML, analisa a estrutura da página e extrai
            informações importantes de forma automática.
        </p>

        <form method="POST">
            <label>Código HTML de exemplo</label>
            <textarea name="codigo_html" required>{{ codigo_html }}</textarea>

            <label>Informação que deseja extrair</label>
            <select name="extrair">
                <option value="titulo" {% if extrair == "titulo" %}selected{% endif %}>Título da página</option>
                <option value="paragrafos" {% if extrair == "paragrafos" %}selected{% endif %}>Parágrafos</option>
                <option value="links" {% if extrair == "links" %}selected{% endif %}>Links</option>
            </select>

            <button type="submit">Analisar HTML com BeautifulSoup</button>
        </form>

        <a class="link-api" href="#">Ver exemplo de extração feita pela biblioteca</a>

        {% if resposta %}
        <section class="resposta">
            <h2>Resposta criada pela BeautifulSoup</h2>

            <p><strong>Tipo de extração:</strong> {{ extrair }}</p>

            {% if resultado %}
                {% for item in resultado %}
                    <p class="item">• {{ item }}</p>
                {% endfor %}
            {% else %}
                <p class="item">Nenhuma informação encontrada no HTML informado.</p>
            {% endif %}

            <p>
                A BeautifulSoup leu o código HTML, organizou a estrutura da página
                e separou os dados solicitados para exibir o resultado.
            </p>
        </section>
        {% endif %}
    </main>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def beautifulsoup_demo():
    codigo_html = """<html>
<head>
    <title>Esquadrão 5</title>
</head>
<body>
    <h1>Os Arquitetos Web</h1>
    <p>BeautifulSoup ajuda a extrair dados de páginas HTML.</p>
    <p>Ela é muito usada em análise de sites e automação.</p>
    <a href="https://python.org">Site do Python</a>
</body>
</html>"""

    extrair = "titulo"
    resposta = False
    resultado = []

    if request.method == "POST":
        codigo_html = request.form.get("codigo_html")
        extrair = request.form.get("extrair")
        resposta = True

        soup = BeautifulSoup(codigo_html, "html.parser")

        if extrair == "titulo":
            titulo = soup.find("title")
            if titulo:
                resultado.append(titulo.get_text())

        elif extrair == "paragrafos":
            paragrafos = soup.find_all("p")
            resultado = [p.get_text() for p in paragrafos]

        elif extrair == "links":
            links = soup.find_all("a")
            resultado = [link.get("href") for link in links if link.get("href")]

    return render_template_string(
        HTML,
        codigo_html=codigo_html,
        extrair=extrair,
        resposta=resposta,
        resultado=resultado
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)