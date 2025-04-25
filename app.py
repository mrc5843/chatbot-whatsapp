@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.form.get('Body').lower().strip()
    print(f"Mensaje recibido: {incoming_msg}")

    respuesta = MessagingResponse()

    # Palabras que activan el mensaje de bienvenida
    saludos = ["hola", "buen dia", "buenos dias", "buenas tardes"]

    if any(saludo in incoming_msg for saludo in saludos):
        respuesta.message("👋 ¡Hola! Bienvenido al asistente virtual.")
        respuesta.message(
            "❓ ¿En qué podemos ayudarte hoy?\n"
            "1️⃣ No puede acceder al sistema SIDE\n"
            "2️⃣ Tiene problemas con un Documento\n"
            "3️⃣ Problemas con un funcionario\n"
            "4️⃣ Problemas con la Firma\n"
            "5️⃣ Otros"
        )
    else:
        respuesta.message(f"Recibido: {incoming_msg}")

    return str(respuesta)