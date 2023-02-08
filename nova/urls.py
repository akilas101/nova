from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/details', views.details, name='details'),
    path('contact', views.contact, name='contact'),
    path('about_us', views.about_us, name='about_us'),
    path('elements', views.elements, name='elements'),
    path('blog', views.blog, name='blog'),
    path('help', views.help, name='help'),
    path('packages', views.packages, name='packages'),
    path('services', views.services, name='services'),
    path('credentials', views.credentials, name='credentials'),
]