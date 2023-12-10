import 'proyect.dart';

class Tarea implements Proyecto {
  final String nombre;
  final String? descripcion;
  EstadoTarea? estado;

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

  String convertirCadena() {
    return '$nombre|$descripcion|$estado';
  }
}

enum EstadoTarea { terminada, postergada, norealizada }
