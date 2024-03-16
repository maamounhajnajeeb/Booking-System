from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Book(models.Model):
    """ 
    booking model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=64)
    person_age = models.SmallIntegerField()
    depart_time = models.DateField(null=True, blank=True)
    return_time = models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.user