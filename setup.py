from cx_Freeze import setup, Executable

# Configuración del ejecutable
setup(
    name="Nombre del ejecutable",
    version="1.0",
    description="Descripción del ejecutable",
    executables=[Executable("generate_img.py")]
)