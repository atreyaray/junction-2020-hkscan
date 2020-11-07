from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

posts = Product.objects.all()

def hello(request):
    context = {
        'posts': posts,
        'title': 'team STEM boys'
    }
    return render(request, 'hello/products.html', context)

def pork(request) :
    context = {
        'posts' : posts,
        'title' : 'team stem boys'
    }
    return render(request, 'hello/pork.html',context)

def beef(request) :
    context = {
        'posts' : posts,
        'title' : 'team stem boys'
    }
    return render(request, 'hello/beef.html',context)

def chicken(request) :
    context = {
        'posts' : posts,
        'title' : 'team stem boys'
    }
    return render(request, 'hello/chicken.html',context)

def products(request) :
    context = {
        'posts': posts,
        'title': 'team stem boys'
    }
    return render(request, 'hello/products.html', context)

def about(request) :
    context ={
        'posts' : posts,
        'title': 'team stem boys'
    }
    return render(request, 'hello/about.html',context)
