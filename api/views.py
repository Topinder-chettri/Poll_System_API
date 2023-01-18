from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework .response import Response
from .models import *
from rest_framework import status
from .serializers import QuestionSerializer,ChoiceSerializer


# Create your views here.
#CREATING API FOR QUESTION

@api_view(['GET', 'POST'])
def questionpost(request):

    if request.method == 'GET':
        snippets = Question.objects.all()
        serializer = QuestionSerializer(snippets, many=True)
        
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def questionall(request, pk):
    
    try:
        snippet = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuestionSerializer(snippet, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = QuestionSerializer(snippet, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   



#CREATING API FOR OPTION

@api_view(['GET', 'POST'])
def Choicepost(request):

    if request.method == 'GET':
        snippets = Choice.objects.all()
        serializer = ChoiceSerializer(snippets, many=True)
        
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Choiceall(request, pk):
  
    try:
        snippet = Choice.objects.get(pk=pk)
    except Choice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChoiceSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ChoiceSerializer(snippet, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = ChoiceSerializer(snippet, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 