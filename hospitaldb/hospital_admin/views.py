from django.http import HttpResponse


def index(request):
    return HttpResponse("Your at the default main-page.")