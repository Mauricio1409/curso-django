from rest_framework.exceptions import APIException


class LibroNoEncontradoError(APIException):
    status_code = 404
    default_detail = "El libro no fue encontrado."
    default_code = "libro_no_encontrado"

class NoTenesPermisosSobreEsteLibroError(APIException):
    status_code = 403
    default_detail = "No tenés permisos sobre este libro."
    default_code = "no_tienes_permisos_sobre_este_libro"


class DatosInvalidosError(APIException):
    status_code = 400
    default_detail = "Los datos proporcionados son inválidos."
    default_code = "datos_invalidos"