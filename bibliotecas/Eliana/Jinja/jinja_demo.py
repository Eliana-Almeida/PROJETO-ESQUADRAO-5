from flask import Flask, request, render_template_string

# =========================================================
# JINJA - ESQUADRAO 5
# OS ARQUITETOS WEB
# Responsavel: Eliana
# =========================================================

# Aqui usamos Flask para abrir a pagina
# e Jinja para preencher o HTML dinamicamente.

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Jinja ao Vivo</title>

<style>
body {
    background: radial-gradient(circle at top, #2a180d, #050816 45%);
    color: white;
    font-family: Arial;
    margin: 0;
    padding: 50px;
}

.container {
    max-width: 760px;
    margin: auto;
    background: #161b22;
    border: 1px solid #d89a52;
    border-radius: 22px;
    padding: 38px;
    box-shadow: 0 0 35px rgba(216,154,82,0.35);
}

h1 {
    color: #d89a52;
    text-align: center;
    font-size: 42px;
}

p {
    line-height: 1.6;
}

label {
    display: block;
    margin-top: 18px;
    color: #f4d3a0;
    font-weight: bold;
}

input, select {
    width: 100%;
    padding: 14px;
    margin-top: 8px;
    border-radius: 10px;
    border: 1px solid #30363d;
    background: #0d1117;
    color: white;
    font-size: 16px;
}

input::placeholder {
    color: #8b949e;
}

button {
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
}

.resultado {
    margin-top: 30px;
    padding: 22px;
    border-radius: 14px;
    background: #0d1117;
    border: 1px solid #3dd68c;
}

.resultado h2 {
    color: #3dd68c;
}

.destaque {
    color: #3dd68c;
    font-weight: bold;
}
.voltar {
    display: inline-block;
    background: #d89a52;
    color: #111;
    border: none;
    padding: 12px 18px;
    border-radius: 10px;
    font-weight: bold;
    cursor: pointer;
    margin: 0 0 25px 0;
    width: auto;
}
.voltar:hover {
    opacity: 0.9;
}
}
</style>
</head>

<body>

<a href="http://127.0.0.1:5000">
    <button class="voltar">← Voltar ao Portal</button>
</a>

<div class="container">

    <h1>JINJA AO VIVO</h1>

    <p>
        Esta pagina mostra o Jinja funcionando na pratica:
        o usuario preenche os campos, o Python recebe os dados
        e o Jinja monta a resposta dinamica na tela.
    </p>

    <form method="POST">
        <label>Nome</label>
        <input type="text" name="nome" placeholder="Digite seu nome completo" value="{{ nome }}" required>

        <label>CPF</label>
        <input type="text" name="cpf" placeholder="000.000.000-00" value="{{ cpf }}" required>

        <label>Curso</label>
        <select name="curso">
            <option {% if curso == "Python para Web" %}selected{% endif %}>Python para Web</option>
            <option {% if curso == "Inteligencia Artificial" %}selected{% endif %}>Inteligencia Artificial</option>
            <option {% if curso == "Automacao Web" %}selected{% endif %}>Automacao Web</option>
            <option {% if curso == "APIs e Sistemas Digitais" %}selected{% endif %}>APIs e Sistemas Digitais</option>
        </select>

        <button type="submit">Renderizar com Jinja</button>
    </form>

    {% if enviado %}
    <div class="resultado">
        <h2>Pagina renderizada pelo Jinja</h2>

        <p><strong>Nome:</strong> {{ nome }}</p>
        <p><strong>CPF:</strong> {{ cpf }}</p>
        <p><strong>Curso:</strong> {{ curso }}</p>

        <p class="destaque">
            O Jinja recebeu os dados enviados pelo Python e montou esta resposta dinamica dentro do HTML.
        </p>
    </div>
    {% endif %}

</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    nome = "Eliana Batista Almeida"
    cpf = "113.***.***-07"
    curso = "Inteligencia Artificial"
    enviado = False

    if request.method == "POST":
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        curso = request.form.get("curso")
        enviado = True

    return render_template_string(
        template,
        nome=nome,
        cpf=cpf,
        curso=curso,
        enviado=enviado
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5011, debug=False, use_reloader=False)