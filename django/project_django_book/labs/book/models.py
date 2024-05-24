from django.db import models
from  author.models import *
# Create your models here.
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    publish_date=models.DateTimeField(auto_now_add=True)
    version=models.IntegerField(default=1)
    latest_version_date=models.DateTimeField(auto_now=True)
    image=models.CharField(max_length=100,null=True)
    author = models.CharField(max_length=100)
    @classmethod
    def addbook(cls, title, version, image, author):
        book = cls(title=title, version=version, image=image, author=author)
        book.save()
        return book