from django.urls import path

from .views import *

urlpatterns = [

    path('d4shb0ard', dashboard),
    path('gdbd', get_data_by_date),

]