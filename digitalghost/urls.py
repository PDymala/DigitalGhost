from django.urls import path, include
from detector import views
urlpatterns = [
    path('', include('website.urls')),
    path('detector', include('detector.urls')),
]
