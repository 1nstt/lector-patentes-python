Se realiza la deteccion y lecura con 2 scripts:

Identificar.py:
Este script se encarga de identificar posibles patentes dentro de una imagen utilizando algoritmos de procesamiento de imágenes. Uno de los algoritmos utilizados es el detector de bordes de Canny, que detecta contornos dentro de la imagen. Estos contornos se filtran según su área para identificar aquellos que podrían ser patentes. El parámetro del área es configurable, permitiendo ajustes según las necesidades específicas. Una vez que se identifica la región de interés, el script recorta la imagen y genera una nueva imagen que contiene solo la patente.

leermatricula.py:
Este script se encarga de leer la patente de la imagen recortada generada por "identificar.py". Utiliza la biblioteca EASYOCR, una herramienta de reconocimiento óptico de caracteres (OCR) que facilita la lectura de texto en imágenes. EASYOCR es conocida por su precisión y capacidad para reconocer texto en múltiples idiomas y formatos. El script devuelve la matrícula como una cadena de texto, permitiendo su uso posterior en aplicaciones o bases de datos.


Caso ejemplo: En el caso ejemplo se puede utilizar la imagen que se encuentra guardada como "auto1.jpg". Primero, ejecutando el script "identificar.py" se obtendrá la nueva imagen de la región de la patente guardada en otro archivo llamado "matricula_1.jpg". Posteriormente, se ejecuta el script "leermatricula.py" el cual se encargará de leer los caracteres de "matricula_1.jpg" y los imprimirá en la consola.


Nota Importante:
Este lector fue desarrollado como parte de un proyecto universitario para una asignatura. No ha sido exhaustivamente probado ya que no estaba destinado para su venta o uso comercial. Me aseguré de que funcionara para los casos específicos necesarios para calificar en el curso. Por lo tanto, dependiendo del uso que se le quiera dar, es posible que se requiera un testeo más profundo y quizás algunas correcciones adicionales.
