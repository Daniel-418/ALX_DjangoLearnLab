from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=(models.CASCADE))

    def __str__(self):  #pyright: ignore
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):  #pyright: ignore
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.PROTECT)

    def __str__(self):  #pyright: ignore
        return self.name

class UserProfile(models.Model):
    role_choices = [("Admin", "Admin"), ("Librarian", "Librarian"), ("Member", "Member")]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=role_choices)
