from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('meal', views.MealView)
router.register('rating', views.RatingView)

urlpatterns = [
    path('', include(router.urls)),
]