from django.urls import path
from . import views

urlpatterns = [
    path('receive-sms/', views.receive_sms, name='receive_sms'),
]
