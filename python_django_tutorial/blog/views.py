from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'January 06, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 08, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
