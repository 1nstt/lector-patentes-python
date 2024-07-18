import cv2

def detectar_matricula(imagen):
    # Cargar la imagen
    img = cv2.imread(imagen)
    
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar un desenfoque gaussiano para reducir el ruido
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Aplicar la detección de bordes con Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Encontrar contornos en la imagen
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filtrar contornos que podrían ser una matrícula
    matriculas = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 6000:  # Ajustar este umbral según el tamaño de las matrículas en tu imagen
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            if len(approx) == 4:
                matriculas.append(approx)

    return matriculas

def guardar_matriculas(imagen, matriculas):
    # Cargar la imagen
    img = cv2.imread(imagen)

    # Guardar cada matrícula detectada en una nueva imagen
    for i, matricula in enumerate(matriculas):
        x, y, w, h = cv2.boundingRect(matricula)
        matricula_recortada = img[y:y+h, x:x+w]
        cv2.imwrite(f'matricula_{i+1}.jpg', matricula_recortada)

# Prueba del código
ruta_imagen = 'auto1.jpg'  # Ruta de la imagen de entrada
matriculas_detectadas = detectar_matricula(ruta_imagen)
guardar_matriculas(ruta_imagen, matriculas_detectadas)
print("Número de matrículas detectadas y guardadas:", len(matriculas_detectadas))


