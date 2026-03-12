from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# O código agora vai procurar a chave no "cofre" do Railway!
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")

@app.route('/', methods=['GET'])
def home():
    return "SGP Bot está Online e a funcionar!", 200

@app.route('/slack/interatividade', methods=['POST'])
def slack_interatividade():
    print("Sucesso! Alguém clicou no botão no Slack!")
    return jsonify({"status": "recebido"}), 200

@app.route('/enviar-teste', methods=['GET'])
def enviar_teste():
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "channel": "#teste",
        "text": "Novo projeto aguardando aprovação!",
        "blocks": [
            {
                "type": "header",
                "text": {"type": "plain_text", "text": "🔔 NOVO PROJETO (SGP)"}
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "*Projeto:* Campanha de Verão 2026\n*Cliente:* Marca Exemplo\n*Lake Atual:* Commercial Lake"}
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "📍 *Ação Requerida:*\nO orçamento foi aprovado. Qual o caminho do projeto?"}
            },
            {
                "type": "actions",
                "elements": [
                    {"type": "button", "text": {"type": "plain_text", "text": "🧠 Precisa Estratégia"}, "style": "primary", "value": "estrategia"},
                    {"type": "button", "text": {"type": "plain_text", "text": "⚡ Fluxo Ágil (Sem Estratégia)"}, "value": "agil"}
                ]
            }
        ]
    }
    
    resposta = requests.post(url, headers=headers, json=payload)
    return jsonify({"status": "Card enviado!"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
