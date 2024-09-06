from rest_framework.response import Response
from rest_framework import status


def handle_response(data: dict, status_code: int = status.HTTP_200_OK) -> Response:
    """Retorna una Respuesta HTTP con un cuerpo y un código de estado personalizados

    Args:
        data (dict): Cuerpo de la respuesta
        status_code (int): Code de estado HTTP (Preferiblemente de la clase status de rest_framework)
    """
    return Response({"msg": "ok", "body": data}, status=status_code)


def response_error_handler(msg: str,  status_code: int, body: dict = None) -> Response:
    """Retorna una Respuesta HTTP con un mensaje y un código de estado personalizados

    Args:
        msg (str): Mensaje de error
        status_code (int): Code de estado HTTP (Preferiblemente de la clase status de rest_framework)
    """
    data = {"msg": msg, "body": body} if body else {"msg": msg}
    return Response(data, status=status_code)


def body_validator(data: dict, required_fields: list = []) -> bool:
    """Valida que los campos requeridos esten presentes en el cuerpo de la petición
    Adicionalmente se pueden Implementar validaciones mas complejas en este apartado

    Args:
        data (dict): Cuerpo de la petición
        required_fields (list): Lista de campos requeridos

    Returns:
        bool: True si todos los campos requeridos estan presentes, False en caso contrario
    """
    for field in required_fields:
        if field not in data:
            return False

    return True
