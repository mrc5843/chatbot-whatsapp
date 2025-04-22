from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Chatbot activo 😎"

@app.route('/webhook', methods=['POST'])
def webhook():
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
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)