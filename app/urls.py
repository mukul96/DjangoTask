from .views import UserViewSet,Check
from rest_framework.routers import DefaultRouter
from django.urls import path
from django.urls import include


router = DefaultRouter()
router.register(r'api', UserViewSet, basename='user')
urlpatterns = router.urls
app_detail = UserViewSet.as_view({
    'get': 'retrieveDetail',
    'put':'updateDetail',
})


# #from test_rest.urls import router
#
# for url in router.urls:
#     print(url.__dict__)

urlpatterns = [


    # path('users', UserViewSet.as_view({'get': 'list'}), name='users'),
    # path('users/<int:pk>', UserViewSet.as_view({'get': 'retrieve'}), name='users'),
    # path('users', UserViewSet.as_view({'post': 'create'}), name='users'),
    path('', include(router.urls)),
    path('retrieveDetail/<int:pk>', app_detail,name='retreive'),
    path('list',Check.as_view({'get':'list'}),name='list')


]