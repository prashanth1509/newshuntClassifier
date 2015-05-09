from django.http import HttpResponse
 
def index(request):
    return HttpResponse('This page shows a list of most recent posts.')