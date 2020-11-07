from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        'type': 'pork',
        'author': 'HK Scan',
        'product_name': 'Tenderloin Steak (Pork)',
        'Type' : 'succulent farm-grown Finnish pork tenderloin. We recommend roasting it.',
        'Recipe': 'Our favorite is crackling pork, you can find the recipe here',
        'RecipeLink': 'https://www.hk.fi/reseptit',
        'media': 'https://hkruokatalo.studio.crasman.fi/pub/Kuvat/Tuotekuvat2/3661.jpg?c=system_1024x',
        'Price' : '10',
        'recipe_name': 'crackling pork',
        'content': '69420',
        'date_posted': 'Nov 7 2020',
        'recipe_main': 'https://www.hk.fi/reseptit/resepti/crackling-pork-joulukinkku/'

    },
    {
        'author': 'HK Scan',
        'product_name': 'Tenderloin Steak (Beef)',
        'Type': 'succulent farm-grown Finnish beef tenderloin. We making a burger!.',
        'Recipe': 'We can back the classic burger, you can find the recipe here',
        'Price': '10',
        'media': 'https://hkruokatalo.studio.crasman.fi/pub/Kuvat/Tuotekuvat2/3437.jpg?c=system_1024x',
        'recipe_main': 'https://www.hk.fi/reseptit/resepti/original-burger/',
        'recipe_name' : 'original burger',
        'content': '69420',
        'date_posted': 'Nov 7 2020'
    },
    {
        'author': 'HK Scan',
        'product_name': 'Vegan Nuggets',
        'Type': 'the perfect fried snacks while making sustainable choices for the world',
        'Price': '7',
        'Recipe' : 'Eat them as is !',
        'media': 'https://hkruokatalo.studio.crasman.fi/pub/Kuvat/Tuotekuvat2/7856.jpg?c = system_1024x',
        'content': '69420',
        'date_posted': 'Nov 7 2020'
    }
    
    # {
    #     'author': 'HK Scan',
    #     'title': 'Production location:',
    #     'product_name': 'Tampere',
    #     'media': '',
    #     'content': '69420',
    #     'date_posted': 'Nov 7 2020'
    # },
    # {
    #     'author': 'HK Scan',
    #     'title': 'Product name:',
    #     'product_name': 'Tenderloin Steak',
    #     'media': '',
    #     'content': '69420',
    #     'date_posted': 'Nov 7 2020'
    # },
]

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
