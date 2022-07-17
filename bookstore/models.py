from django.db import models
from .data import *


class Authors(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.IntegerField()

    @staticmethod
    def create_authors():
        for i in authors:
            author = Authors(first_name=i['first_name'], last_name=i['last_name'], age=i['age'])
            author.save()

    def __str__(self):
        return f"{self.pk} {self.last_name}"


class Books(models.Model):
    title = models.CharField(max_length=128)
    released_year = models.IntegerField()
    description = models.TextField()
    author_id = models.IntegerField()
    relations = models.ForeignKey(Authors, on_delete=models.CASCADE, blank=True, null=True)

    @staticmethod
    def create_books():
        for i in books:
            book = Books(title=i['title'], released_year=i['released_year'], description=i['description'],
                         author_id=i['author_id'])
            book.save()

    def __str__(self):
        return f"{self.pk} {self.title}"
