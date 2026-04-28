from django.urls import path
from .views import *
urlpatterns = [
    # endpoint for  the get and post request
   path('blogpost/', BlogView.as_view(), name='blogpost'),
   #endpoinmt for patch and delete request
   path('blogpost/<int:pk>/', BlogView.as_view(), name='blogpost-detail'),
]