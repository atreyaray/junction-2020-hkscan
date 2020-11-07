from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        'author': 'HK Scan',
        'title': 'Product:',
        'product_name': 'Tenderloin Steak',
        'media': 'https://hkruokatalo.studio.crasman.fi/pub/Kuvat/Tuotekuvat2/3661.jpg?c=system_1024x',
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

    return render(request, 'hello/home.html', context)
