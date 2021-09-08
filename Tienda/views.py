from django.shortcuts import render

def store(request):
     context = {}
     return render(request, 'Tienda/store.html', context)

def cart(request):
     context = {}
     return render(request, 'Tienda/cart.html', context)

def checkout(request):
      context = {}
      return render(request, 'Tienda/checkout.html', context)