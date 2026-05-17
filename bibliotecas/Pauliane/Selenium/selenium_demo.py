
from flask import Flask, render_template_string, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Selenium AO VIVO</title>

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

input{

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

<a href="/" class="voltar">← Voltar ao Portal</a>

<div class="container">

<h1>SELENIUM AO VIVO</h1>

<p>
Esta página demonstra a biblioteca Selenium funcionando AO VIVO:
automação de navegador, acesso real a páginas web e captura
de informações automaticamente.
</p>

<form method="POST">

<label>Site para automação</label>

<input
type="text"
name="site"
value="{{site}}"
required
>

<button type="submit">
Executar Automação Selenium
</button>

</form>

{% if resultado %}

<div class="resposta">

<h2>Resposta da Automação</h2>

<p><strong>Site acessado:</strong> {{site}}</p>

<p><strong>Título encontrado:</strong> {{titulo}}</p>

<p>
<strong>Status:</strong>
<span class="status">
Automação executada com sucesso
</span>
</p>

<p>
O Selenium abriu o navegador real,
acessou o site automaticamente
e capturou o título da página AO VIVO.
</p>

</div>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def selenium_demo():

    resultado = False

    titulo = ""

    site = "https://www.google.com"

    if request.method == "POST":

        site = request.form.get("site")

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            )
        )

        driver.get(site)

        titulo = driver.title

        driver.quit()

        resultado = True

    return render_template_string(
        HTML,
        resultado=resultado,
        titulo=titulo,
        site=site
    )

if __name__ == "__main__":
    app.run(debug=True, port=5005)