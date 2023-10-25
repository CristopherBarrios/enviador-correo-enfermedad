import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_correo(nombre, apellido, id_orden, datos_orden, destinatario):
    # Configura la información del remitente
    # destinatario = 'exitosuccesso@gmail.com'
    remitente = 'exitosuccesso@gmail.com'
    contraseña = 'hgzc ayna jawo mqjq'  # NO almacenes tu contraseña en el código real

    asunto = "Gracias " + nombre + " " + apellido + " Orden: "+ id_orden
    
    mensaje = "Gracias por escoger a Almira en breve confirmaremos lo que solicistaste, este es tu pedido, cualquier duda puedes mandar un correo: \n"
    mensaje += "\n"
    mensaje += datos_orden

    destinatarios = []
    destinatarios.append(remitente)
    destinatarios.append(destinatario)


    # Crea un objeto MIME para el correo electrónico
    correo = MIMEMultipart()
    correo['From'] = remitente
    correo['To'] = ", ".join(destinatarios)
    correo['Subject'] = asunto

    # Adjunta el mensaje al cuerpo del correo
    cuerpo = mensaje
    correo.attach(MIMEText(cuerpo, 'plain'))

    # Configura el servidor SMTP de Gmail
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587

    # Inicia una conexión segura con el servidor SMTP
    conexion = smtplib.SMTP(servidor_smtp, puerto_smtp)
    conexion.starttls()

    # Inicia sesión en la cuenta de Gmail
    conexion.login(remitente, contraseña)

    # Envía el correo electrónico
    texto_del_correo = correo.as_string()
    conexion.sendmail(remitente, destinatarios, texto_del_correo)

    # Cierra la conexión con el servidor SMTP
    conexion.quit()

# enviar_correo("Entrega","Este es un nuevo mensaje mas decente")