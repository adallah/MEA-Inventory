from rest_framework.exceptions import PermissionDenied
class Headers:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        accepted = ['/admin', '/sitemap.xml','/favicon.ico','/static','/dashboard','/jet']
        allowed = True
        for item in accepted:
            if request.path.startswith(item):
                allowed=True
        if request.META['SERVER_NAME'] == "testserver":
            allowed = True
        domains = ['http://localhost:8080','http://10.113.108.231','http://inventory-portal.cisco.com','https://inventory-portal.cisco.com/']
        origin = request.META.get('HTTP_ORIGIN')
        if origin and origin in domains :
            response['Access-Control-Allow-Origin'] = origin
            response['Access-Control-Allow-Headers'] = "Origin, Content-Type, Authorization"
            response['Access-Control-Allow-Methods'] = "POST, GET, OPTIONS, DELETE, PATCH"
            response['Access-Control-Allow-Credentials'] = "true"
        if request.path.startswith('/uploads'):
            return response
        if allowed:
            return response
        raise PermissionDenied(detail=None, code=None)
