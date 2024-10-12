from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import StatectlServer


# Create your views here.
def index(request):
    try:
        server = StatectlServer.objects.all()
    except StatectlServer.DoesNotExist:
        raise Http404('Server not found ...')
    return render(request, 'statectl/index.html', {'server': server})
