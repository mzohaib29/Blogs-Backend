from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
from apiBase.models import User
from .serializers import UserRegistrationSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'apiBase/token/refresh/',
        'apiBase/token/verify/'
    ]
    return Response(routes)

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        # print("debug", request.data)
        try: 
            print(request.data)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            print(user)
            return Response(
                {
                    "user": serializer.data,
                    "message": "User created successfully.",
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            print(e)
            return Response({'error': "Password do not match"})