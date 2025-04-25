@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.form.get('Body').lower().strip()
    print(f"Mensaje recibido: {incoming_msg}")

    respuesta = MessagingResponse()

    # Palabras que activan la bienvenida
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
    elif incoming_msg == "1":
        respuesta.message("✅ Entendido. Revisaremos el acceso al sistema SIDE.")
    elif incoming_msg == "2":
        respuesta.message("📄 Por favor, indique el tipo de problema con el documento.")
    elif incoming_msg == "3":
        respuesta.message("👤 ¿Podría describir el problema con el funcionario?")
    elif incoming_msg == "4":
        respuesta.message("🖊️ ¿Tiene error con la Firma Electrónica o con el sistema?")
    elif incoming_msg == "5":
        respuesta.message("📬 Describa brevemente su situación para poder ayudarle.")
    else:
        respuesta.message("🤖 No entendí ese mensaje. Por favor escriba un número del 1 al 5 o un saludo para ver el menú.")

    return str(respuesta)