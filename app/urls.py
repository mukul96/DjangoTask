from .views import UserViewSet
from django.urls import path




urlpatterns = [



    path('users', UserViewSet.as_view({'get':'listUsers','post':'createUser'}),name='listUsers'),
    path('users/<int:pk>', UserViewSet.as_view({'get':'retrieveDetail','delete':'deleteUser','put':'updateUser'}),name='retreive'),



]