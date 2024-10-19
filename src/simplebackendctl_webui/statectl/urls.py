from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/statectl/create', views.create, name='create'),
    path('admin/statectl/delete', views.delete, name='delete'),
    path('admin/statectl/update', views.update, name='update'),
]
