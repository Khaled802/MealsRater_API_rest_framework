from django.shortcuts import render
from .serializers import RatingSerializer, MealSerializer
from rest_framework import viewsets 
from .models import Meal, Rating
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

# Create your views here.


class UserView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        try:
            User.objects.create_user(username=username, password=password)
            Json = {'details': 'created successfully'}
            status_code = status.HTTP_201_CREATED
        except Exception as e:
            Json =  {'details': f'failed creation {e}'}
            status_code = status.HTTP_400_BAD_REQUEST
        
        return Response(Json, status=status_code)


class MealView(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(methods=['post'], detail=True)
    def rate_meal(self, request, pk=None):
        author = request.user
        meal = Meal.objects.get(pk=pk)
        try:
            stars = request.data['stars']
            rating, _ = Rating.objects.get_or_create(auth=author, meal=meal)
            rating.stars = stars
            rating.save()
            serializer = RatingSerializer(rating)
            Json = {
                'details': f'the {meal} rating is updated',
                'result': serializer.data
            }
            status_code = status.HTTP_200_OK
        except:
            Json = {'details': 'the stars is not provided'}
            status_code = status.HTTP_400_BAD_REQUEST
            
        
        return Response(Json, status=status_code)
            
        

class RatingView(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


