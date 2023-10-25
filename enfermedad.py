import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model 
import numpy as np
import os

def diagnosticar(image_path):
    # image_path = 'input/paapapa.png'
    image_size = (224, 224)

    # Obtiene la ruta absoluta del directorio actual del archivo Python
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Concatena la ruta absoluta con la ubicación del archivo del modelo
    model_path = os.path.join(current_dir, 'chekpoint', 'model_checkpoint.h5')

    # Carga el modelo
    model = load_model(model_path)

    # Carga la imagen y rediménsionala al tamaño que el modelo espera
    img = image.load_img(image_path, target_size=image_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    # Realiza la predicción
    prediction = model.predict(img_array)

    # Obtiene la etiqueta correspondiente a la clase con mayor probabilidad
    predicted_class = np.argmax(prediction)

    # Obtén las etiquetas de clases del generador
    #class_labels = list(train_generator.class_indices.keys())

    class_labels = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
    max_prob = np.max(prediction)

    # print(f'Maximum probability: {max_prob}')

    # Imprime la imagen y el resultado
    # plt.imshow(img)
    # plt.axis('off')
    # plt.title("Predicción: " + class_labels[predicted_class])
    # plt.show()
    # print("Predicción: " + class_labels[predicted_class])
    return "Predicción: " + class_labels[predicted_class] + "\n" + f'Maximum probability: {max_prob}'


# if __name__ == '__main__':

#         # Obtiene la ruta absoluta del directorio actual del archivo Python
#     current_dir = os.path.dirname(os.path.abspath(__file__))

#     # Concatena la ruta absoluta con la ubicación del archivo del modelo
#     image_file = os.path.join(current_dir, 'input', 'paapapa.png')
#     diagnosticar(image_file)