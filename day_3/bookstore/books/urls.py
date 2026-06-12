from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('<int:id>/', views.show_book, name='show_book'),
    path('<int:id>/delete/', views.delete_book, name='delete_book'),
    path('add/', views.add_book, name='add_book')
]