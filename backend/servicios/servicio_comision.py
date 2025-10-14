from repositorios.repositorio_comision import RepositorioComision


class ServicioComision:
    def __init__(self):
        self.repo = RepositorioComision()

    def crear_comision(self, id_usuario, descripcion):
        return self.repo.insertar(id_usuario, descripcion)

    def listar_comisiones_usuario(self, id_usuario):
        return self.repo.listar_por_id_usuario(id_usuario)

    def listar_todas(self):
        return self.repo.listar_todas_con_usuario()

    def despachar_comision(self, id_comision):
        estado = self.repo.obtener_estado_por_id(id_comision)
        if estado is None or estado == 'Despachado':
            return False
        return self.repo.marcar_despachado(id_comision)
