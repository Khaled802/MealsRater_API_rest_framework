from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='ratings')
    auth = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self) -> str:
        return f'{self.auth} {self.meal}'

    class Meta:
        unique_together = (('meal', 'auth'),)
        index_together = (('meal', 'auth'),)
