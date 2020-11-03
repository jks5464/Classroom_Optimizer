from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Justin',
        'title': 'First Post',
        'content': 'First Post Content',
        'date': 'nao'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'classroomOptimizer/home.html', context)

def about(request):
    return render(request, 'classroomOptimizer/about.html')
