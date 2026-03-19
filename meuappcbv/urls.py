from django.urls import path
from .views import view

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
]