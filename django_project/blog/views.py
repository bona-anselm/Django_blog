from django.shortcuts import render


posts = [
    {
        'author': 'Bona Anselm',
        'title': 'Blog Post 1',
        'content': 'First Content',
        'date_posted': '21-10-2023'
    },
    {
        'author': 'Anselm',
        'title': 'Blog Post 2',
        'content': 'Second Content',
        'date_posted': '20-10-2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})