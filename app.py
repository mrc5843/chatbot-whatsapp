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
    elif incoming_msg == "1":
        respuesta.message("✅ Favor indícame los siguientes datos para poder ayudarle:\n\n- Rut\n- Usuario Active Directory")
    elif incoming_msg == "2":
        respuesta.message("📄 Favor indícame los siguientes datos para poder ayudarle:\n\n- Número de documento")
    elif incoming_msg == "3":
        respuesta.message("👤 Favor indícame los siguientes datos para poder ayudarle:\n\n"
                          "- Número(s) de el(los) Documento(s) Afectado(s).\n"
                          "- Rut del funcionario con el problema\n"
                          "- Breve descripción del problema")
    elif incoming_msg == "4":
        respuesta.message("🖊️ Para obtener la firma digital, siga estos pasos:\n\n"
                          "1- Ingresar a https://firma.digital.gob.cl/ra/ con su clave única\n"
                          "2- Presionar el botón \"NUEVA SOLICITUD +\"\n"
                          "3- Seleccionar Propósito y Teléfono, posteriormente presionar SOLICITAR\n"
                          "4- Una vez terminada la solicitud debe esperar que los entes autorizados autoricen su firma\n"
                          "5- Una vez ya adquirido su certificado en la página principal https://firma.digital.gob.cl/ra/system/home#/certificados debe apretar el símbolo del ojo al lado derecho.\n"
                          "6- Presionar VER CODIGO QR y luego OBTENER QR\n"
                          "7- Una vez generado debe escanearlo con la app de su celular, se recomienda usar Microsoft Authenticator.")
    elif incoming_msg == "5":
        respuesta.message("📬 Favor indícame los siguientes datos para poder ayudarle:\n\n"
                          "- Número(s) de el(los) Documento(s) Afectado(s).\n"
                          "- Nombre, Cargo y Unidad.\n"
                          "- Usuario Active Directory del(los) afectado(s).\n"
                          "- Breve descripción del problema.")
    else:
        respuesta.message("🤖 No entendí ese mensaje. Por favor escriba un número del 1 al 5 o un saludo para ver el menú.")

    return str(respuesta)

# Código para que funcione en Render correctamente
if __name__ == '__main__':
    puerto = int(os.environ.get('PORT',

