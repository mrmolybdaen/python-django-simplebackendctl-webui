from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import StatectlServer


# Create your views here.
def index(request):
    """This view will display the management table of servers

        One can set states to MAINT or UP here.
    """
    try:
        server = StatectlServer.objects.all()
    except StatectlServer.DoesNotExist:
        raise Http404('Server not found ...')
    return render(request, 'statectl/index.html', {'server': server})


def servers_manage(request):
    """This view will manage server configurations

        One can choose to create, update or delete a server from the list.
    """

    try:
        server = StatectlServer.objects.all()
    except StatectlServer.DoesNotExist:
        raise Http404('Server not found ...')

    return render(request, 'statectl/manage.html', {'server': server})

def servers_create(request):
    """This view will present a form to create a new server

        One can create a new server.
    """

    return render(request, 'statectl/create.html', {'server': server})

def servers_update(request):
    """This view will present a form to update a server

        One can update a server entry with new information here.
    """
    return render(request, 'statectl/update.html', {'server': server})

def servers_delete(request):
    """This view will present a form to delete a server

        One can delete a server which does not exist anymore.
    """

    return render(request, 'statectl/delete.html', {'server': server})
