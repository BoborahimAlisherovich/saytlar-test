from django.urls import path
from . import views

urlpatterns = [
    path('', views.scan_view, name='scan'),
]
