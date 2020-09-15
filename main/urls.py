from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new', views.makeShow),
    path('create', views.newShow),
    path('shows', views.show),
    path('shows/<int:num>/edit', views.edit),
    path('update/<int:num>', views.update),
    path('shows/<int:num>/delete', views.delete),
    path('shows/<int:num>', views.info),
]