from flask import Flask, request, jsonify, render_template
from correo import enviar_correo
from flask_cors import CORS 
from enfermedad import diagnosticar
import os

app = Flask(__name__)
CORS(app, resources={r"/predict-image": {"origins": ["http://localhost:3000", "https://succes-4a1e9.firebaseapp.com"]}})

@app.route('/procesar-orden', methods=['POST'])
def procesar_orden():
    data = request.get_json()  # Obtener datos de la solicitud POST 

    order_data = data['orderData']

    correo_usuario = data['correo']
    nombre_usuario = data['nombre']
    apellido_usuario = data['apellido']
    order_data_orderId = str(order_data['orderId'])

    order_data_date = order_data['date']

# Itera a través de la lista de productos en el pedido
    productos_usuario = ""
    for index, product_item in enumerate(order_data['products'], start=1):
        product_name = product_item['product']['name']
        offer_percentage = product_item['product']['offerPercentage']
        product_price = product_item['product']['price']
        quantity = product_item['quantity']

        productos_usuario += f"\n\nProducto {index}:\nNombre del Producto: {product_name}\nOferta: {offer_percentage or 'N/A'}\nPrecio: Q{product_price:.2f}\nCantidad: {quantity}"


    # Accede a la dirección
    address = order_data['address']

    # Imprime los campos de la dirección
    direccion_usurio = f"\nTítulo: {address['addressTitle']}\nCiudad: {address['city']}\nNombre: {address['fullName']}\nTeléfono: {address['phone']}\nEstado: {address['state']}\nCalle: {address['street']}"

    # Accede a la precio
    precio = str(order_data['totalPrice'])

    mensaje = f"ID de la orden: {order_data_orderId}" + "\n" + f"Fecha: {order_data_date}" + "\n" + "\n" + "\n" + f"Productos de la Orden: {productos_usuario}" + "\n" + "\n" + "\n" + f"Dirección: {direccion_usurio}" + "\n" + "\n" + "\n" + f"Precio total: {precio}"


    # print("order_data: ")
    # print( order_data)

    # print("data a observar: ")
    # print(mensaje)

    # Para enviar un correo electrónico, puedes llamar a tu función enviar_correo
    enviar_correo(nombre_usuario, apellido_usuario, order_data_orderId, mensaje, correo_usuario)
    
    return jsonify({'message': 'Orden procesada con éxito'})

@app.route('/probando')
def probando():
    return "Hola que tal"

@app.route('/predict-image', methods=['POST'])
def predict_image():
        # Define la carpeta temporal para guardar imágenes
    TEMP_IMAGE_FOLDER = 'temp_images'

    # Asegúrate de que la carpeta exista, o créala si es necesario
    os.makedirs(TEMP_IMAGE_FOLDER, exist_ok=True)
    try:
        image_file = request.files['image']
        if image_file:
            # Genera un nombre de archivo único
            image_filename = os.path.join(TEMP_IMAGE_FOLDER, 'temp_image.png')
            image_file.save(image_filename)
            result = diagnosticar(image_filename)
            # result = diagnosticar(image_file)

            # Opcional: elimina el archivo guardado después de usarlo
            os.remove(image_filename)

            return jsonify(result)
        else:
            return jsonify({'error': 'No se proporcionó una imagen válida'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port = 5000, debug = True)
