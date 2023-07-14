# # views.py
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.views import APIView
# from django.contrib.auth import authenticate
# from rest_framework.response import Response


# class LoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             })
#         else:
#             return Response({'error': 'Invalid credentials'}, status=401)





from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.generics import (CreateAPIView,)
# from rest_framework.permissions import (AllowAny,)
# from .serializers import UserSerializers

# class SignupAPIView(CreateAPIView):
#     serializer_class = UserSerializers
#     permission_classes = [AllowAny]

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        print(token)

        # Add custom claims
        
        token['email'] = user.email
        token['username'] = user.username
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'newapi/token',
        'newapi/token/refresh'
    ]
    return Response(routes)

