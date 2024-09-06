from rest_framework.response import Response
from rest_framework import status


def handle_response(
    data: dict, status_code: int = status.HTTP_200_OK, msg: str = "ok"
) -> Response:
    """Returns a HTTP Response with a custom message and status code

    Args:
        data (dict): Response body
        status_code (int): Http status code (Preferably from the status class of rest_framework)
    """

    return Response({"msg": msg, "body": data}, status=status_code)


def response_error_handler(msg: str, status_code: int, body: dict = None) -> Response:
    """Returns a HTTP Response with a custom message and status code

    Args:
        msg (str): Error message
        status_code (int): Http status code (Preferably from the status class of rest_framework)
    """

    data = {"msg": msg, "body": body} if body else {"msg": msg}
    return Response(data, status=status_code)


def body_validator(data: dict, required_fields: list = []) -> bool:
    """Validates if all the required fields are present in the request body

    Args:
        data (dict): request body
        required_fields (list): required fields list

    Returns:
        bool: returns True if all the required fields are present in the request body
    """
    for field in required_fields:
        if field not in data:
            return False

    return True
