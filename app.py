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
    respuesta.message(f"Recibido: {incoming_msg}")
    
    return str(respuesta)