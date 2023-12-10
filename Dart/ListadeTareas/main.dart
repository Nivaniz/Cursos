import 'dart:io';

import 'controlers/agregar_tarea.dart';
import 'controlers/eliminar_tarea.dart';
import 'controlers/ver_tarea.dart';

void main() {
  while (true) {
    print('\n-------- Menú de Tareas --------');
    print('1. Agregar Tarea');
    print('2. Ver Tareas');
    print('3. Eliminar Tarea');
    print('4. Salir');
    stdout.write('Selecciona una opción (1-4): ');
    final entrada = stdin;

    String opcion = stdin.readLineSync() ?? '';

    switch (opcion) {
      case '1':
        print("Seleccionaste agregar tarea");
        agregarTarea();
        break;

      case '2':
        print("Selecionaste ver una tarea");
        print("Coloca el nombre de la tarea que deseas ver: ");
        final nombre = entrada.readLineSync();
        verTarea(nombre ?? '');
        break;

      case '3':
        print("Selecionaste borrar una tarea");
        print("Coloca el nombre de la tarea que deseas eliminar: ");
        final nombre = entrada.readLineSync();
        eliminarTarea(nombre ?? '');
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
