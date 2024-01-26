import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Cargar datos desde el archivo Excel
archivo_excel = 'empleados.xlsx'  # Reemplaza con el nombre de tu archivo Excel
df = pd.read_excel(archivo_excel)

# Dimensiones de la imagen de fondo
fondo_path = 'fondo.png'  # Reemplaza con el nombre de tu imagen de fondo
fondo = Image.open(fondo_path)
ancho_fondo, alto_fondo = fondo.size

# Crear una imagen para cada fila en el DataFrame
for indice, fila in df.iterrows():
    # Crear una copia de la imagen de fondo
    nueva_imagen = fondo.copy()

    # Inicializar el objeto de dibujo
    dibujo = ImageDraw.Draw(nueva_imagen)



    fuente = ImageFont.truetype("times.ttf", 20)  # Puedes cambiar "arial.ttf" por la fuente que desees


    # Escribir los datos en la nueva imagen
    x, y = 240, 30  # Posición inicial
    for clave, valor in fila.items():
        texto = f"{valor}"
        dibujo.text((x, y), texto, font=fuente, fill='black')
        y += 25  # Ajustar el espaciado vertical según sea necesario

    # Guardar la nueva imagen
    # Se generará una imagen para cada fila
    nueva_imagen.save(f'output_{indice + 1}.png')
