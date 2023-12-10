import 'dart:io';
import '../utils/convertir.dart';

void verTarea(String nombre) {
  try {
    final archivo = File('./task.txt');
    if (archivo.existsSync()) {
      final contenido = archivo.readAsLinesSync();
      contenido.forEach((tareaLocal) {
        if (tareaLocal.contains(nombre)) {
          final tarea = convertirTarea(tareaLocal);
          print("Este es el objeto tarea -->");
          print("Nombre: ${tarea.nombre}");
          print("Descripción: ${tarea.descripcion}");
          print("Estado: ${tarea.estado}");
        }
      });
    } else {
      print("El archivo es inexistente");
    }
  } catch (e) {
    print("Ocurrio un error");
  }
}
