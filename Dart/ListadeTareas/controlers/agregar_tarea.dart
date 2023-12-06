import 'dart:io';
import '../models/taks.dart';

void agregarTarea() {
  final entrada = stdin;
  try {
    final archivo = File('./task.txt');
    if (archivo.existsSync()) {
      final contenido = archivo.readAsStringSync();

      print("Nombre de la Tarea:");
      final nombre = entrada.readLineSync() ?? 'Tarea sin nombre';
      print("Descripción de la tarea:");
      final descripcion = entrada.readLineSync();
      // ignore: unused_local_variable
      final tarea = Tarea(nombre, descripcion: descripcion);
      archivo.writeAsStringSync(contenido + '\n' + tarea.convertirCadena());
    } else {
      print("El archivo es inexistente");
    }
  } catch (e) {
    print("Ocurrio un error");
  }
}
