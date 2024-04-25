from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('chair', views.chair),
    path('table', views.table),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create')
]