from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        'author': 'HK Scan',
        'title': 'Calves separated from mothers so far:',
        'content': '69420',
        'date_posted': 'Nov 7 2020'
    }
]

def hello(request):
    context = {
        'posts': posts,
        'title': 'team STEM boys'
    }

    return render(request, 'hello/home.html', context)
