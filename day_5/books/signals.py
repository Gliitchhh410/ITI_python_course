from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, ISBN

@receiver(post_save, sender=Book)
def create_book_isbn(sender, instance, created, **kwargs):
    if created:
        ISBN.objects.create(
            book=instance,
            book_title=instance.title,
            author_title=instance.user.username if instance.user else "Unknown Author"
        )
