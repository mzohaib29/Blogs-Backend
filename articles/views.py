from django.shortcuts import render
from rest_framework import status
from .models import Article
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import ArticleSerializers
# from django.http import HttpResponse

# Create your views here.
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all().order_by('date')
    serializer = ArticleSerializers(articles, many=True)
    return Response(serializer.data)
    # return Response(request, 'article_list.html', {'articles': articles})

@api_view(['GET'])
def article_one(request, id):
    articles = Article.objects.get(id = id)
    serializer = ArticleSerializers(articles, many=False)
    return Response(serializer.data)

# @api_view(['POST'])
# def article_create(request):
#     serializer = ArticleSerializers(data=request.data)
#     if not serializer.is_valid():
#         return Response({'Status': status.HTTP_400_BAD_REQUEST, 'Error': serializer.errors})
#     serializer.save()
#     return Response({'Status': status.HTTP_201_CREATED, 'Details': serializer.data, 'Message': 'Data added successfully'})

@api_view(['POST'])
def article_create(request):
        try:
            print(request.data)
            title = request.data.get('title')
            body = request.data.get('body')
            thumb = request.FILES.get('thumb')
            author_name = request.data.get('author_name')
            author_image = request.FILES.get('author_image')
            # Create a new blog object
            blog = Article(title=title, body=body, thumb=thumb, author_name = author_name, author_image = author_image)
            blog.save()
            return JsonResponse({'body': '123', 'title': '123', 'thumb': 'thumb', 'author_name': 'author_name', 'author_image': 'author_image'})
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'error'})

# @api_view(['POST'])
# def article_create(request):
#         title = request.POST.get('title')
#         body = request.POST.get('body')
#         # thumb = request.FILES.get('thumb')
#         # print(thumb)
#         # Create a new blog object
#         blog = Article(title=title, body=body)
#         blog.save()
#         return JsonResponse({'message': 'Blog created successfully.', 'title': title, 'body': body})

@api_view(['PUT'])
def article_update(request, id):
    try: 
        articles = Article.objects.get(id = id)
        serializer = ArticleSerializers(articles, data = request.data, partial = True)
        if not serializer.is_valid():
            return Response({'Status': 404, 'Error': serializer.errors})
        serializer.save()
        return Response({'Status': 200, 'Details': serializer.data, 'Message': "Data updated successfully"})
    except Exception as e:
        return Response({'Status': 403, 'Message': 'Invalid id'})

@api_view(['DELETE'])
def article_delete(request, id):
    try:
        articles = Article.objects.get(id = id)
        articles.delete()
        return Response({'Status': 200, 'Message': "Data deleted successfully"})
    except Exception as e:
        return Response({'Status': 403, 'Message': "Invalid id"})


def article_detail(request, slug):
    articles = Article.objects.get(slug=slug)
    return render(request, 'article_details.html', {'article': articles})

# @login_required(login_url="/accounts/login/")
# def article_create(request):
#     return render(request, 'article_create.html')

