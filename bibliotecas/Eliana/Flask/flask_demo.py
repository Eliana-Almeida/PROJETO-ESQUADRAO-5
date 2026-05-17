from flask import Flask, request

# =========================================================
# FLASK - ESQUADRAO 5
# OS ARQUITETOS WEB
# Responsavel: Eliana
# =========================================================

# Flask cria aplicacoes web usando Python.
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    resultado = ""

    # Quando o formulario e enviado, o Python recebe os dados
    if request.method == "POST":
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        curso = request.form.get("curso")

        resultado = f"""
        <div class="resultado">
            <h2>Dados recebidos pelo Python</h2>
            <p><strong>Nome:</strong> {nome}</p>
            <p><strong>CPF:</strong> {cpf}</p>
            <p><strong>Curso:</strong> {curso}</p>
            <p>O Flask recebeu o formulario, processou os dados e devolveu esta resposta no navegador.</p>
        </div>
        """

    return f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Flask ao Vivo</title>

        <style>
            body {{
                background: radial-gradient(circle at top, #2a180d, #050816 45%);
                color: white;
                font-family: Arial;
                margin: 0;
                padding: 50px;
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
                font-size: 16px;
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

            input::placeholder {{
                color: #8b949e;
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
        </style>
    </head>

    <body>
        <div class="container">
            <h1>FLASK AO VIVO</h1>

            <p>
                Esta pagina prova que o Flask esta funcionando:
                o usuario preenche o formulario, o Python recebe os dados
                e devolve uma resposta dinamica no navegador.
            </p>

            <form method="POST">
                <label>Nome</label>
                <input type="text" name="nome" placeholder="Digite seu nome completo" required>

                <label>CPF</label>
                <input type="text" name="cpf" placeholder="000.000.000-00" required>

                <label>Curso</label>
                <select name="curso">
                    <option>Python para Web</option>
                    <option>Inteligencia Artificial</option>
                    <option>Automacao Web</option>
                    <option>APIs e Sistemas Digitais</option>
                </select>

                <button type="submit">Enviar para o Python</button>
            </form>

            {resultado}
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5010, debug=True)