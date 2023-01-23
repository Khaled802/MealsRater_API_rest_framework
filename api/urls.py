from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken.views import obtain_auth_token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token

router = DefaultRouter()
router.register('meal', views.MealView)
router.register('rating', views.RatingView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth-token/', obtain_auth_token),
   
]

@receiver(signal=post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created, **kwarg):
    if created:
        Token.objects.create(user=instance)