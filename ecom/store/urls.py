from django.urls import path
from . import views
urlpatterns=[
    path('show_data/',views.show_data,name='show_data'),
    path('insert_data/',views.insert_data,name='insert_data'),
] 