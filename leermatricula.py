import easyocr
import cv2
import os
import re
def leer_matricula(image_path):
    # Inicializa el lector de EasyOCR
    reader = easyocr.Reader(['en'])

    # Verifica si la imagen existe
    if not os.path.exists(image_path):
        print(f'Error: No se encontró la imagen en la ruta especificada: {image_path}')
        return ''

    image = cv2.imread(image_path)
    if image is None:
        print(f'Error: No se pudo abrir la imagen en la ruta especificada: {image_path}')
        return ''

    # Convierte la imagen a RGB (OpenCV la carga en BGR por defecto)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Utiliza EasyOCR para leer el texto en la imagen
    result = reader.readtext(image_rgb)

    # Imprime los resultados crudos
    print("Resultados crudos de EasyOCR:")
    for res in result:
        print(res)

    # Variable para almacenar el texto de la matrícula
    matricula = ''

    # Procesa los resultados para encontrar la matrícula
    for (bbox, text, prob) in result:
        print(f'Detectado: {text} con una probabilidad de {prob:.2f}')
        # Aquí actualizamos la matrícula sin importar la probabilidad
        if matricula == '' or prob > 0.55:  # Ajustamos el umbral de probabilidad
            matricula = text

    # Imprime la matrícula encontrada en la terminal
    print(f'Matrícula: {matricula}')

    # Opcional: muestra la imagen con el texto detectado
    #for (bbox, text, prob) in result:
 #       (top_left, top_right, bottom_right, bottom_left) = bbox
 #       top_left = tuple(map(int, top_left))
  #      top_right = tuple(map(int, top_right))
   #     bottom_right = tuple(map(int, bottom_right))
    #    bottom_left = tuple(map(int, bottom_left))
        
     #   cv2.rectangle(image_rgb, top_left, bottom_right, (0, 255, 0), 2)
      #  cv2.putText(image_rgb, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    #Muestra la imagen (opcional)
   # import matplotlib.pyplot as plt
    #plt.imshow(image_rgb)
    #plt.axis('off')
    #plt.show()

    return matricula

def limpiar_matricula(matricula):
    # Eliminar todos los caracteres que no sean letras o números (A-Z, a-z, 0-9)
    matricula_limpia = re.sub(r'[^A-Za-z0-9]', '', matricula)
    return matricula_limpia




# Ejemplo de uso de la función
image_path = 'matricula_1.jpg'  # Actualiza esta ruta según corresponda
matricula = leer_matricula(image_path)
print(f'La matrícula leída es: {matricula}')
matriculaprocesada= limpiar_matricula(matricula)
print(f'La matricula limpia es : {matriculaprocesada}')
