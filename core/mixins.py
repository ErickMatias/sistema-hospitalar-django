from django.core.exceptions import PermissionDenied


class CargoPermitidoMixin:

    cargos_permitidos = []

    def dispatch(self, request, *args, **kwargs):

        funcionario = request.user.funcionario

        if funcionario.cargo not in self.cargos_permitidos:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)