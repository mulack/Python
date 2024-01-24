# https://cdnjs.com/ - scripts html

from flask import Flask, render_template
from flask_socketio import SocketIO, send #

# cria o site
app = Flask(__name__)
app.config["SECRET"] = "meusamigosisso34343fdf" # chave de seguranca
socketio = SocketIO(app, cors_allowed_origins="*") # cria a conexão entre diferentes máquinas


# criar paginas
@socketio.on("message") 
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True) # envia a mensagem para todo mundo conectado no site

# cria a página do site
@app.route("/") 
def home():
    return render_template("index.html") # essa página vai carregar esse arquivo html

if __name__ == "__main__":
    socketio.run(app, host='localhost') # define que o app vai rodar local