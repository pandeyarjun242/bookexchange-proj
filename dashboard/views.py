from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# Create your views here.

def add(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['author']:
            book = Book()
            book.title = request.POST['title']
            book.author = request.POST['author']
            book.image = request.FILES['image']
            book.pub_date = request.POST['date']
            book.owner = request.user
            book.save()
        else:
            return redirect('home')
    else:
        return render(request, 'add.html')
def detail(request , product_id):
    product = get_object_or_404(Product, pk = product_id)
    return render(request, 'detail.html', {'product':product})
def bid(request, product_id):
    return render(request,'detail.html')
