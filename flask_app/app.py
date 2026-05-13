from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'ESQUADRÃO 5: OS ARQUITETOS WEB'

@app.route('/api')
def api():
    return {
        'mensagem': 'API funcionando com Flask'
    }

if __name__ == '__main__':
    app.run(debug=True)