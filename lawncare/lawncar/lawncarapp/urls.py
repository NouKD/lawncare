from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('main', views.main, name='main'),
    path('blog_single', views.blog_single, name='blog_single'),
]