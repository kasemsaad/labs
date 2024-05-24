from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=200)

    @classmethod
    def get_all(cls):
        return [(auth.id,auth.name) for auth in cls.objects.all()]
      
    @classmethod
    def getauthorbyid(cls, id):
            return cls.objects.get(id=id)
