from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.urls import reverse
from .models import Book, Category, ISBN

class BookstoreTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.category = Category.objects.create(name='Fiction')

    def test_book_title_validation(self):
        # Title too short (< 10)
        book1 = Book(title='Short', desc='A short book title test', rate=4.5, user=self.user)
        with self.assertRaises(ValidationError):
            book1.full_clean()

        # Title too long (> 50)
        long_title = 'A' * 51
        book2 = Book(title=long_title, desc='A long book title test', rate=4.5, user=self.user)
        with self.assertRaises(ValidationError):
            book2.full_clean()

        # Title correct length
        book3 = Book(title='Valid Book Title', desc='A valid book title test', rate=4.5, user=self.user)
        book3.full_clean()  # Should not raise exception

    def test_category_name_validation(self):
        # Category name too short (< 2)
        cat = Category(name='A')
        with self.assertRaises(ValidationError):
            cat.full_clean()

        # Category name valid
        cat2 = Category(name='Valid')
        cat2.full_clean()  # Should not raise exception

    def test_isbn_signal(self):
        # Creating a book should trigger the signal to create an ISBN
        book = Book.objects.create(title='Awesome Django Book', desc='Learn Django', rate=5.0, user=self.user)
        book.categories.add(self.category)

        # Retrieve the ISBN
        isbn = ISBN.objects.get(book=book)
        self.assertEqual(isbn.book_title, 'Awesome Django Book')
        self.assertEqual(isbn.author_title, 'testuser')
        self.assertEqual(len(isbn.isbn_number), 13)

    def test_views_require_login(self):
        # Create book requires login
        response = self.client.get(reverse('book_create'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login

        # Delete book requires login
        book = Book.objects.create(title='Another Great Book', desc='More Django', rate=4.0, user=self.user)
        response = self.client.get(reverse('book_delete', args=[book.pk]))
        self.assertEqual(response.status_code, 302)  # Should redirect to login
