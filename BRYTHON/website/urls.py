from django.urls import path
from .views import index, ajaxme

urlpatterns = [
    path('', index, name='home'),
    path('ajaxme', ajaxme, name='ajaxme'),
]