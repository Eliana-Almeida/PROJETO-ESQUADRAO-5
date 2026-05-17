from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Django AO VIVO</title>

<style>

*{
    box-sizing:border-box;
}

body{
    margin:0;
    min-height:100vh;
    font-family:Arial, Helvetica, sans-serif;

    background:
    radial-gradient(circle at center,
    rgba(220,150,70,0.20),
    transparent 35%),
    #050816;

    color:white;
}

.voltar{
    position:fixed;
    top:30px;
    left:30px;

    background:#e0a050;
    color:#111;

    text-decoration:none;

    padding:12px 20px;

    border-radius:8px;

    font-weight:bold;

    box-shadow:0 0 20px rgba(224,160,80,.4);
}

.container{

    width:92%;
    max-width:720px;

    margin:80px auto;

    background:#171c23;

    border:1px solid #d99545;

    border-radius:18px;

    padding:42px 34px;

    box-shadow:0 0 40px rgba(217,149,69,.35);
}

h1{

    text-align:center;

    color:#e0a050;

    font-size:38px;

    margin-bottom:20px;
}

p{
    line-height:1.7;
    color:#ddd;
}

label{

    display:block;

    margin-top:18px;
    margin-bottom:8px;

    color:#e8c38f;

    font-weight:bold;
}

input, select{

    width:100%;

    padding:14px;

    border-radius:8px;

    border:1px solid #333;

    background:#070b13;

    color:white;

    font-weight:bold;
}

button{

    width:100%;

    margin-top:24px;

    padding:14px;

    border:none;

    border-radius:10px;

    background:#e0a050;

    color:#111;

    font-size:15px;

    font-weight:bold;

    cursor:pointer;
}

button:hover{
    background:#f0b96d;
}

.resposta{

    margin-top:30px;

    border:1px solid #24c36b;

    border-radius:14px;

    padding:24px;

    background:#0d1118;
}

.resposta h2{

    color:#2ecc71;
}

.status{
    color:#2ecc71;
    font-weight:bold;
}

</style>

</head>

<body>

<a href="http://127.0.0.1:5000" class="voltar">
← Voltar ao Portal
</a>

<div class="container">

<h1>DJANGO AO VIVO</h1>

<p>
Esta página demonstra o funcionamento do Django:
rotas, views, processamento de dados e renderização dinâmica.
</p>

<form method="POST">

<label>Nome</label>

<input
type="text"
name="nome"
value="{{nome}}"
required
>

<label>Perfil</label>

<select name="perfil">

<option>Administrador</option>
<option>Desenvolvedor</option>
<option>APIs</option>

</select>

<button type="submit">
Executar Django AO VIVO
</button>

</form>

{% if resultado %}

<div class="resposta">

<h2>Resposta criada pela View do Django</h2>

<p><strong>Nome:</strong> {{nome}}</p>

<p><strong>Perfil:</strong> {{perfil}}</p>

<p>
<strong>Status:</strong>
<span class="status">
Rota processada com sucesso
</span>
</p>

<p>
O Django recebeu os dados pela rota,
processou na view
e devolveu esta resposta HTML.
</p>

</div>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    resultado = False

    nome = "Mohamed"

    perfil = "Administrador"

    if request.method == "POST":

        nome = request.form.get("nome")

        perfil = request.form.get("perfil")

        resultado = True

    return render_template_string(
        HTML,
        resultado=resultado,
        nome=nome,
        perfil=perfil
    )

if __name__ == "__main__":
    app.run(debug=True, port=5012)