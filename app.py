from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def home():
    return "Chatbot activo 😎"

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.form.get('Body')
    print(f"Mensaje recibido: {incoming_msg}")

    respuesta = MessagingResponse()
    mensaje = respuesta.message(f"Recibido: {incoming_msg}")
    
    return str(respuesta)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)