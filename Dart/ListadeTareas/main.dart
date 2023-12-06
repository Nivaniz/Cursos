import 'dart:io';

import 'controlers/agregar_tarea.dart';

void main() {
  while (true) {
    print('\n-------- Menú de Tareas --------');
    print('1. Agregar Tarea');
    print('2. Eliminar Tarea');
    print('3. Ver Tareas');
    print('4. Salir');
    stdout.write('Selecciona una opción (1-4): ');

    String opcion = stdin.readLineSync() ?? '';

    switch (opcion) {
      case '1':
        print("Seleccionaste agregar tarea");
        agregarTarea();
        break;

      case '2':
        var tareas;
        if (tareas.isEmpty) {
          print('No hay tareas para eliminar.');
        } else {
          print('Tareas Actuales:');
        }
        break;

      case '3':
        var tareas;
        if (tareas.isEmpty) {
          print('No hay tareas para mostrar.');
        } else {}
        break;

      case '4':
        print('Saliendo del programa. ¡Hasta luego!');
        exit(0);

      default:
        print('Opción no válida. Inténtalo de nuevo.');
        break;
    }
  }
}
