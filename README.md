# Proyecto de Detección y Lectura de Patentes

Este proyecto incluye dos scripts principales para la detección y lectura de patentes de vehículos a partir de imágenes: `identificar.py` y `leermatricula.py`. Fue desarrollado como parte de un proyecto universitario y está diseñado para reconocer y extraer matrículas de imágenes mediante técnicas de procesamiento de imágenes y reconocimiento óptico de caracteres (OCR).

## Descripción de los Scripts

### 1. `identificar.py`
Este script es responsable de identificar posibles patentes dentro de una imagen. Utiliza algoritmos de procesamiento de imágenes, como el detector de bordes de Canny, para detectar contornos en la imagen. Los contornos se filtran según su área para identificar aquellos que podrían corresponder a patentes. El parámetro del área es configurable, permitiendo ajustes según las necesidades específicas del usuario.

**Funcionamiento:**
- Detecta bordes en la imagen usando el algoritmo de Canny.
- Filtra los contornos detectados según su área.
- Identifica la región de interés que podría contener una patente.
- Recorta la imagen para generar una nueva imagen que solo contiene la patente.

**Salida:**
- Una imagen recortada con la patente identificada.

### 2. `leermatricula.py`
Este script se encarga de leer la patente de la imagen recortada generada por `identificar.py`. Para esto, se utiliza la biblioteca EASYOCR, una potente herramienta de reconocimiento óptico de caracteres (OCR) que es capaz de reconocer texto en múltiples idiomas y formatos con gran precisión.

**Funcionamiento:**
- Toma la imagen recortada que contiene la patente.
- Utiliza EASYOCR para leer y extraer los caracteres de la matrícula.
- Imprime la matrícula en la consola como una cadena de texto.

## Caso de Ejemplo

1. **Identificación de la Patente:**
   - Utiliza la imagen guardada como `auto1.jpg`.
   - Ejecuta `identificar.py` para identificar la región de la patente.
   - Se generará una nueva imagen recortada llamada `matricula_1.jpg` que contiene la patente.

2. **Lectura de la Patente:**
   - Ejecuta `leermatricula.py` para leer los caracteres de la matrícula desde `matricula_1.jpg`.
   - El script imprimirá la matrícula detectada en la consola.

## Nota Importante

Este lector fue desarrollado como parte de un proyecto universitario y no ha sido exhaustivamente probado para su uso comercial. Funciona correctamente en los casos específicos necesarios para la calificación en el curso. Sin embargo, dependiendo del uso que se le quiera dar, es posible que se requiera un testeo más profundo y posibles ajustes adicionales.

## Requisitos

- Python 3.x
- Librerías necesarias: 
  - OpenCV (cv2)
  - EASYOCR
  - numpy

Puedes instalar las dependencias utilizando `pip`:

```bash
pip install opencv-python-headless easyocr numpy




Cómo Usar
Asegúrate de que tienes instaladas todas las dependencias.
Coloca la imagen que deseas analizar en el mismo directorio que los scripts.
Ejecuta el script identificar.py para obtener la imagen recortada de la patente.
Luego, ejecuta leermatricula.py para leer y extraer la matrícula de la imagen recortada.
