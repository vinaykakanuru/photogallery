from django.urls import path
from photosapp.views import home, add_photo, view_photo

urlpatterns = [
    path('', home, name='home'),
    path('photo/<str:pk>', view_photo, name='view_photo'),
    path('add/', add_photo, name='add_photo'),
]
