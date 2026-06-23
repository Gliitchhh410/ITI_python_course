import random
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Category(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2, message="Category name must be at least 2 characters long.")]
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(10, message="Book title must be between 10 and 50 characters long."),
            MaxLengthValidator(50, message="Book title must be between 10 and 50 characters long.")
        ]
    )
    desc = models.TextField()
    rate = models.FloatField()
    views = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    categories = models.ManyToManyField(Category, related_name='books')

    def __str__(self):
        return self.title

def generate_isbn():
    return "".join([str(random.randint(0, 9)) for _ in range(13)])

class ISBN(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='isbn')
    author_title = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)
    isbn_number = models.CharField(max_length=50, unique=True, default=generate_isbn)

    class Meta:
        verbose_name = "ISBN"
        verbose_name_plural = "ISBNs"

    def __str__(self):
        return f"{self.book_title} - {self.isbn_number}"

    