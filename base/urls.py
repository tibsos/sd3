from django.urls import path

from .views import *

urlpatterns = [

    path('', landing),

    path('b', button_click),
    
    path('c', receive_contact_info),

]