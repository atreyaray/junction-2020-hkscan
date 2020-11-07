from django.urls import path

from . import views

urlpatterns = [    
    path('', views.hello, name='hello'),
    path('recipes', views.recipes, name='recipe_page'),
    path('products', views.recipes, name='products_page')
]
