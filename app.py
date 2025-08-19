from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<nome>/<prontuario>/<instituicao>")
def identificacao(nome, prontuario, instituicao):
    return render_template("identificacao.html",
                           nome=nome,
                           prontuario=prontuario,
                           instituicao=instituicao)

@app.route("/contextorequisicao")
def contexto():
    user_agent = request.headers.get("User-Agent")
    ip_remoto = request.remote_addr
    host_app = request.host
    return render_template("contexto.html",
                           user_agent=user_agent,
                           ip_remoto = ip_remoto,
                           host_app = host_app)

if __name__ == "__main__":
    app.run(debug=True)