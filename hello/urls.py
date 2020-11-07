from django.urls import path

from . import views

urlpatterns = [    
    path('', views.hello, name='hello'),
    path('pork', views.pork, name='pork'),
    path('beef', views.beef, name='beef'),
    path('chicken', views.chicken, name='chicken'),
    path('products', views.products, name='products_page'),
    path('about', views.about, name='about_page')

]
