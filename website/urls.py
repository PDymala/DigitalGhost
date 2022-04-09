from django.urls import path
from . import views
from detector import views as det


urlpatterns = [
   path('', views.homepage, name='home'),
   path('detector', det.detector, name='detector')
]