from rest_framework.views import exception_handler
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # Si la respuesta es None, significa que no se ha manejado la excepción, la maneja django
    if not response:
        logger.error(f"Excepción no manejada: {exc} - Contexto: {context}")
        return None

    # Personalizar la respuesta de error
    custom_response_data = {
        "status": "error",
        "status_code": response.status_code,
        "details": response.data
    }
    logger.error(f"Excepción manejada: {exc} - Contexto: {context} - Respuesta personalizada: {custom_response_data}")
    return Response(custom_response_data, status=response.status_code)
