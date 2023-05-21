from django.conf import settings
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status


class responseHelper:

    @staticmethod
    def test_response(text_message):

        result = {
            'mensagem': text_message,
            'version': settings.VERSION_ENV
        }

        return JsonResponse(result, status=206)

    @staticmethod
    def json_success_response(result_json_object, msg, total=None, version_warning=""):

        result = {
            'message': msg,
            'success': True,
        }

        if total is not None and total <= 0:
            return responseHelper.json_not_found_response(result_json_object)
        else:
            if total:
                result["total"] = total

        if result_json_object:
            result["result"] = result_json_object

        if settings.INCLUDE_API_INFO:
            result['api-info'] = {
                'version': settings.VERSION_ENV,
                'version_warning': version_warning
            }

        return Response(result, status=status.HTTP_200_OK)

    @staticmethod
    def json_not_found_response(result_json_object, version_warning=""):
        msg = 'Consulta realizada com sucesso - Sem resultados'

        result = {
            'success': False,
            'message': msg
        }

        if result_json_object:
            result['result'] = result_json_object

        if settings.INCLUDE_API_INFO:
            result['api-info'] = {
                'version': settings.VERSION_ENV,
                'version_warning': version_warning
            }

        return Response(result, status.HTTP_404_NOT_FOUND)

    @staticmethod
    def json_error_response(status_code_number, error_text, error_description, version_warning=""):
        if not error_description:
            error_description = 'Não foi possível processar sua solicitação. Tente novamente em instantes.'

        response_obj = {
            'success': False,
            'message': error_text,
            'error_description': error_description
        }

        if settings.INCLUDE_API_INFO:
            response_obj['api-info'] = {
                'version': settings.VERSION_ENV,
                'version_warning': version_warning
            }

        return Response(response_obj, status=status_code_number)

    @staticmethod
    def not_authorized_response():
        return responseHelper.json_error_response(status.HTTP_401_UNAUTHORIZED, 'Unauthorized', f'Requisição não autorizada')

    @staticmethod
    def invalid_verb_response(allowed_mehod="POST"):
        return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST, 'invalid_request', f'Método {allowed_mehod} é requerido')

    @staticmethod
    def invalid_request_error_response(text):
        return responseHelper.json_error_response(status.HTTP_403_FORBIDDEN, 'invalid_request', text)

    @staticmethod
    def login_error_response(text):
        return responseHelper.json_error_response(status.HTTP_403_FORBIDDEN, 'invalid_login', text)

    @staticmethod
    def invalid_access_token_response():
        return responseHelper.json_error_response(status.HTTP_403_FORBIDDEN, 'invalid_login', 'Access Token inválido')

    @staticmethod
    def invalid_backoffice_token_response():
        return responseHelper.json_error_response(status.HTTP_403_FORBIDDEN, 'invalid_login', 'Backoffice Token inválido')

    @staticmethod
    def customer_inactive_response():
        return responseHelper.json_error_response(status.HTTP_403_FORBIDDEN, 'invalid_customer', 'A empresa está inativa ou bloqueada. Favor entrar em contato com o atendimento')

    @staticmethod
    def invalid_operation_error_response(text):
        return responseHelper.json_error_response(status.HTTP_403_FORBIDDEN, 'invalid_operation', text)
