from django.shortcuts import render
from django.http import HttpResponse

#dummy data is a list[] of dicts{}
posts = [
    {
        'author': 'Robert JM',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 15, 2020'

    },
    {
        'author': 'Rose LM',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 16, 2020'

    }
]
# Create your views here.

#home function for user going to blog home page
#context dict key posts allows insertion of argument in return function
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

#logic for about page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'} )

