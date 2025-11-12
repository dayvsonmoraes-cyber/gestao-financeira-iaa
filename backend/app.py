from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensagem": "API funcionando com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)

