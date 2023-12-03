from pathlib import Path


# Regresar el path absoluto de la carpeta principal
def absPath(file):
    return str(Path(__file__).parent.absolute() / file)
