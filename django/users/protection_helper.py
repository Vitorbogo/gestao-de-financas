from user_agents import parse

class protection_helper:

    @staticmethod
    def is_valid_requestor(request):
        ua_string = request.headers.get('User-Agent','')
        if ua_string == '':
            return False
        
        ua = parse(ua_string)
        if ua.is_bot:
            return False

        return True