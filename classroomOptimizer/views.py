from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Justin Siu, Reegan Jiang',
        'title': 'Classroom Optimizer',
        'content': 'This web application optimizes seating and table arrangement of a classroom. This optimization will adhere to distancing policies in order to prevent the spread of viruses and diseases.',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'classroomOptimizer/home.html', context)

def about(request):
    return render(request, 'classroomOptimizer/about.html')
