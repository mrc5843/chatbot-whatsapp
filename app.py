from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.form.get('Body', '').lower().strip()
    print(f"Mensaje recibido: {incoming_msg}")

    respuesta = MessagingResponse()

    if any(palabra in incoming_msg for palabra in ["hola", "buen dia", "buenos dias", "buenos días", "buenas tardes"]):
        respuesta.message("👋 ¡Hola! Bienvenido al asistente virtual.")
        respuesta.message(
            "❓ ¿En qué podemos ayudarte hoy?\n"
            "1️⃣ No puede acceder al sistema SIDE\n"
            "2️⃣ Tiene problemas con un Documento\n"
            "3️⃣ Problemas con un funcionario\n"
            "4️⃣ Problemas con la Firma\n"
            "5️⃣ Otros"
        )
    elif incoming_msg in ["1", "2", "3", "4", "5"]:
        opciones = {
            "1": "✅ Entendido. Revisaremos el acceso al sistema SIDE.",
            "2": "📄 Por favor, indique el tipo de problema con el documento.",
            "3": "👤 ¿Podría describir el problema con el funcionario?",
            "4": "🖊️ ¿Tiene error con la Firma Electrónica o con el sistema?",
            "5": "📬 Describa brevemente su situación para poder ayudarle."
        }
        respuesta.message(opciones[incoming_msg])
    else:
        respuesta.message("🤖 No entendí ese mensaje. Por favor escriba un número del 1 al 5 o un saludo para ver el menú.")

    return str(respuesta)

# Ejecutar con el puerto que entrega Render
if __name__ == '__main__':
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=puerto)
