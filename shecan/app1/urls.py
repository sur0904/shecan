from django.urls import path
from .views import home,register,api_data

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('api_data/', api_data, name='api_data'),
    

]