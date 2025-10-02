from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books/index.html', context)


def detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
    }
    return render(request, 'books/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('books:detail', book.pk)
    else:
        form = BookForm()
    context = {
        'form': form,
    }
    return render(request, 'books/create.html', context)


@login_required
def delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('books:index')


@login_required
def update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:detail', book.pk)
    else:
        form = BookForm(instance=book)
    context = {
        'book': book,
        'form': form,
    }
    return render(request, 'books/update.html', context)