from django.db import models

# base models for category and cast
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Cast(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, help_text="e.g., Actor, Director")

    def __str__(self):
        return self.name

# abstract model because movies and serries are the same, so inherit from one class
class ProductionBase(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    
    # Many-to-Many relations
    categories = models.ManyToManyField(Category, related_name="%(class)ss")
    casts = models.ManyToManyField(Cast, related_name="%(class)ss")
    # Dynamically name the names the reverse relationship as movies and seriess (with an s) respectively,
    # preventing Django from throwing a naming collision error.
    
    poster_image = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


# Concrete Models inheriting from the Base
class Movie(ProductionBase):
    pass


class Series(ProductionBase):
    pass