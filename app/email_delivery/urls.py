from django.urls import path
from .views import EmailDelivery

urlpatterns = [
    path('email', EmailDelivery.as_view(), name='email_delivery')
]
