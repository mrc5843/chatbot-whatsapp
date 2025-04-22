from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    mensaje = request.form.get('Body')
    respuesta = MessagingResponse()
    mensaje_respuesta = respuesta.message()

    if 'hola' in mensaje.lower():
        mensaje_respuesta.body("¡Hola! ¿En qué puedo ayudarte hoy?")
    elif 'precio' in mensaje.lower():
        mensaje_respuesta.body("Nuestros productos van desde $10.000 CLP. ¿Hay algo que te interese?")
    else:
        mensaje_respuesta.body("No entendí bien tu mensaje. ¿Puedes repetirlo?")

    return str(respuesta)

if __name__ == '__main__':
    app.run(debug=True)