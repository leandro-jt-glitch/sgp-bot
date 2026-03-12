from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota de teste para sabermos se o servidor está online
@app.route('/', methods=['GET'])
def home():
    return "SGP Bot está Online e a funcionar!", 200

# Rota que vai receber os cliques dos botões do Slack
@app.route('/slack/interatividade', methods=['POST'])
def slack_interatividade():
    return jsonify({"status": "recebido"}), 200

# Rota que vai receber os avisos do ClickUp
@app.route('/clickup/webhook', methods=['POST'])
def clickup_webhook():
    return jsonify({"status": "recebido"}), 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
