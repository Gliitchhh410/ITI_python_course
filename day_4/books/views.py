from django.shortcuts import render
from .models import Book
# Create your views here.

# Read (All)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# READ (Single)
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.views += 1  # Increment view counter
    book.save()
    return render(request, 'books/book_detail.html', {'book': book})

# CREATE
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Create'})

# UPDATE
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Update'})

# DELETE
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})