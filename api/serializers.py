from rest_framework import serializers
from .models import Meal, Rating

class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = ('name', 'description', 'get_rating_number', 'get_average_rating')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'




