from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from rest_framework.views import APIView
from .serializers import CarSerializer

# Create your views here.

# Представления на основе функций

# @api_view(['GET', 'POST'])
# @csrf_exempt
# def car_list(request, format=None):
#     if (request.method == 'GET'):
#         cars = Car.objects.all()
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data)
#     elif (request.method == 'POST'):
#         serializer = CarSerializer(data=request.data)
#         if (serializer.is_valid()):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# @csrf_exempt
# def car_detail(request, pk, format=None):
#     try:
#         car = Car.objects.get(pk=pk)
#     except Car.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if (request.method == 'GET'):
#         serializer = CarSerializer(car)
#         return Response(serializer.data)
#     elif (request.method == 'PUT'):
#         serializer = CarSerializer(car, data=request.data)
#         if (serializer.is_valid()):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif (request.method == 'DELETE'):
#         car.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# Представления на основе классов, наследуемых от базового класса APIView

# class CarList(APIView):
#     def get(self, request, format=None):
#         cars = Car.objects.all()
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = CarSerializer(data=request.data)
#         if (serializer.is_valid()):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class CarDetail(APIView):
#     def get_object(self, pk):
#         try:
#             car = Car.objects.get(pk=pk)
#         except Car.DoesNotExist:
#             return Http404
        
#     def get(self, request, pk, format=None):
#         serializer = CarSerializer(self.get_object(pk))
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         serializer = CarSerializer(self.get_object(pk), data=request.data)
#         if (serializer.is_valid()):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         car = self.get_object(pk)
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Представления на основе классов, с использованием миксинов

# from rest_framework import mixins, generics

# class CarList(mixins.ListModelMixin,
#               mixins.CreateModelMixin,
#               generics.GenericAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class CarDetail(mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin,
#                 mixins.DestroyModelMixin,
#                 generics.GenericAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# Общие представления на основе классов

from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'cars': reverse('car-list', request=request, format=format)
    })

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
  
class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetailt(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer