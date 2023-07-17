from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'apiBase/token/refresh/',
        'apiBase/token/verify'
    ]
    return Response(routes)