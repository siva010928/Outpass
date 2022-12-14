from django.db import models


class User(models.Model):
    short=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_number=models.CharField(max_length=100)
    clicks=models.IntegerField(default=0)
    isAllowed=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f"{self.email}"