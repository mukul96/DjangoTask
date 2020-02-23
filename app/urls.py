from .views import UserViewSet
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token





urlpatterns = [



    path('users', UserViewSet.as_view({'get':'listUsers','post':'createUser'}),name='listUsers'),
    path('users/<int:pk>', UserViewSet.as_view({'get':'retrieveDetail','delete':'deleteUser','put':'updateUser'}),name='retreive'),
    path('api-token-auth/', obtain_jwt_token),



]