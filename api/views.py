from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
    data = request.data
    # print(data)
    serializer = TaskSerializer(data = request.data)
    if not serializer.is_valid():
        return Response({'Status': 403, 'message': 'Something went wrong'})
    serializer.save()
    # print(serializer.data)
    return Response({'staus': 200, 'details': serializer.data, 'message': 'Data sent successfully'})