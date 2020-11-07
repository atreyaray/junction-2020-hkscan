from django.urls import path

from . import views

urlpatterns = [    
    path('', views.hello, name='hello'),
    path('pork', views.pork, name='pork'),
    path('products', views.products, name='products_page'),
    path('about', views.about, name='about_page')
]
