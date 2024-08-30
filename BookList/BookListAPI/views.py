from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
# Create your views here.

@csrf_exempt
def books(request):
    books = Book.objects.all()
    dict_rc = [model_to_dict(instance) for instance in books]
    dict = { 'books': dict_rc }
    print(dict)
    if request.method == 'GET':
        return JsonResponse(dict, status=200)
    elif request.method == 'POST':
        print(request.POST)
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        book = Book(title=title, author=author, price=price, inventory=inventory)
        print(model_to_dict(book))
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)
    return JsonResponse(model_to_dict(book), status=201)