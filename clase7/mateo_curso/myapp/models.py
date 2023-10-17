from django.db import models

# Create your models here.
class Curso(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.name