from django.shortcuts import render


def homepage(request):
    return render(request, 'Blog.html')
# Create your views here.
