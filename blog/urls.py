from django.urls import path
#imports views.py from current directory
from . import views
#'' makes it the home page, name should be unique for reverse lookup
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]