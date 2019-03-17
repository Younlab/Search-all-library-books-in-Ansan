from django.urls import path, include

urlpatterns = [
    path('search/', include('search.urls')),
    path('delivery/', include('email_delivery.urls'))
]
