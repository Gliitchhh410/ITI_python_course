from django.shortcuts import render
from django.http import HttpResponse, Http404


# Create your views here.

book_list = [
    {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin"},
]


def list_books(request):
    html_content = "<h1>List of Books</h1><ul>"
    for book in book_list:
        html_content += f"<li>{book['id']}: {book['title']} by {book['author']}</li>"
    html_content += "</ul>"
    return HttpResponse(html_content)


def show_book(request, id):
    for book in book_list:
        
        if book["id"] == id:
            return HttpResponse(f"<h1>{book['title']}</h1><p>By {book['author']}</p>")
    raise Http404(f"Book with id {id} not found")


def delete_book(request, id):
    for book in book_list:
        if book["id"] == id:
            book_list.remove(book)
            return HttpResponse(f"Book with id {id} deleted")
    raise Http404(f"Book with id {id} not found")


def add_book(request):
    id = request.GET.get("id")
    for book in book_list:
        if book["id"] == id:
            return HttpResponse(f"Book with id {id} already exists")
    title = request.GET.get("title")
    author = request.GET.get("author")
    book_list.append({"id": int(id), "title": title, "author": author})
    return HttpResponse(f"Book with id {id} added")