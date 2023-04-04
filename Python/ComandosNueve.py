from pathlib import Path

# Librerias & Documentacion

# Absolute path
# c:\9838\OneDrive

# Relative path
path = Path("ecommerce")
path.exists()  # Al imprimirlo regresa un True o un False

# Si queremos crear uno llamamos al método
# path = Path("emails")
# path.mkdir() make directory y para borrarlo es path.rmdir() remove directory

# path = Path()
# path.glob('*.*') para buscar TODOS directorios y archivos en el path actual
# path.glob('*.py')
# path.glob('*.xl')

pathN = Path()
for file in pathN.glob('*.py'):
    print(file)  # Imprimir todos los archivos

# Vamos a descargar paquetes para trabajar con las hojas xls de excel
# Se pueden descargar más paquetes en PypI