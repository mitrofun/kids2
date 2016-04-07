from django.shortcuts import render


def home(request):
    context = {
        'hello': 'Hello world'
    }
    return render(request, 'cms/index.html', context)
