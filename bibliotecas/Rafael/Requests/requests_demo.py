from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Requests ao Vivo</title>
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

        input, select {
            width: 100%;
            padding: 13px;
            border-radius: 8px;
            border: 1px solid #303744;
            background: #080c14;
            color: #fff;
            font-weight: bold;
            outline: none;
        }

        input:focus, select:focus {
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

        .status {
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
        <h1>Requests ao Vivo</h1>

        <p>
            Esta página mostra a biblioteca Requests funcionando na prática:
            envio de requisição, simulação de resposta externa, status HTTP
            e retorno processado para o usuário.
        </p>

        <form method="POST">
            <label>Nome</label>
            <input type="text" name="nome" value="{{ nome }}" required>

            <label>Tipo de Requisição</label>
            <select name="tipo">
                <option value="GET" {% if tipo == "GET" %}selected{% endif %}>GET - Buscar dados</option>
                <option value="POST" {% if tipo == "POST" %}selected{% endif %}>POST - Enviar dados</option>
                <option value="PUT" {% if tipo == "PUT" %}selected{% endif %}>PUT - Atualizar dados</option>
                <option value="DELETE" {% if tipo == "DELETE" %}selected{% endif %}>DELETE - Remover dados</option>
            </select>

            <label>Site / API de Exemplo</label>
            <input type="text" name="api" value="{{ api }}" required>

            <button type="submit">Enviar requisição com Requests</button>
        </form>

        <a class="link-api" href="#">Ver exemplo de resposta simulada da API</a>

        {% if resposta %}
        <section class="resposta">
            <h2>Resposta recebida pela Requests</h2>

            <p><strong>Nome:</strong> {{ nome }}</p>
            <p><strong>Tipo de requisição:</strong> {{ tipo }}</p>
            <p><strong>API acessada:</strong> {{ api }}</p>
            <p><strong>Status HTTP:</strong> <span class="status">200 OK</span></p>

            <p>
                A biblioteca Requests enviou a requisição, recebeu os dados,
                interpretou a resposta e devolveu o resultado para esta página HTML.
            </p>
        </section>
        {% endif %}
    </main>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def requests_demo():
    nome = "Rafael"
    tipo = "GET"
    api = "https://api.exemplo.com/dados"
    resposta = False

    if request.method == "POST":
        nome = request.form.get("nome")
        tipo = request.form.get("tipo")
        api = request.form.get("api")
        resposta = True

    return render_template_string(
        HTML,
        nome=nome,
        tipo=tipo,
        api=api,
        resposta=resposta
    )

if __name__ == "__main__":
    app.run(debug=True, port=5004)