import 'proyect.dart';
import 'sub_task.dart';

class Tarea implements Proyecto {
  final String nombre;
  final String? descripcion;
  EstadoTarea? estado;

  List<SubTarea> subtareas = [];

  Tarea(this.nombre,
      {this.descripcion = '', this.estado = EstadoTarea.norealizada});

  @override
  void terminarTarea() {
    estado = EstadoTarea.norealizada;
  }

  @override
  void postergarTarea() {
    estado = EstadoTarea.postergada;
  }

  @override
  void realizarTarea() {
    estado = EstadoTarea.terminada;
  }

  void agregarSubTarea(SubTarea subTarea) {
    subtareas.add(subTarea);
  }

  void eliminarSubTarea(int index) {
    subtareas.removeAt(index);
  }

  String convertirCadena() {
    return '$nombre|$descripcion|$estado';
  }
}

enum EstadoTarea { terminada, postergada, norealizada }
