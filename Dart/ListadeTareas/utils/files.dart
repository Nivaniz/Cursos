import 'dart:io';

void main() {
  // Proyecto -> Abstraccion
  // Tarea
  // Subtarea

  try {
    final archivo = File('./task.txt');
    if (archivo.existsSync()) {
      final contenido = archivo.readAsStringSync();
      print("El contenido es: ${contenido}");

      final nuevoContenido = "María Nacarda";
      archivo.writeAsStringSync(contenido + '\n' + nuevoContenido);
    } else {
      print("El archivo es inexistente");
    }
  } catch (e) {
    print("Ocurrio un error");
  }
}
