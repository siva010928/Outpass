from django.db import models


class User(models.Model):
    short=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_number=models.CharField(max_length=100)
    clicks=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return f"short= {self.short} name= {self.name} email= {self.email} roll= {self.roll_number} clicks= {self.clicks}"