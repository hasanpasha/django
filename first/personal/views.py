from django.http import HttpResponse


def index(request):
    return HttpResponse("<p>Test</p><a><h1>HOME</h1></a><h2>HOME PAGE</h2><p>HELLO, World!</p>")
