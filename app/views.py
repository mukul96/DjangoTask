from rest_framework import viewsets
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from  .serializers import UserSerializer
from rest_framework import status
from django.http import Http404
from django.db.models import  Q
from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page_size=5




class UserViewSet(CustomPageNumberPagination,viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer


    def get_object(self, pk):
        try:
            return UserInfo.objects.get(pk=pk)
        except UserInfo.DoesNotExist:
            raise Http404("user does not exist")


    def listUsers(self, request):
        name = request.GET.get('name', None)
        q_object = Q()
        if name is not None:
            q_object |= Q(first_name__icontains=name)
            q_object |= Q(last_name__icontains=name)
        userObjects = UserInfo.objects.filter(q_object)
        order=request.GET.get('sort', None)
        if order is not None:
            userObjects = userObjects.order_by(order)
        serializedData = UserSerializer(userObjects, many=True)
        data = self.paginate_queryset(serializedData.data, request)

        return Response(data,status=status.HTTP_200_OK)


    def createUser(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("user created",status=status.HTTP_201_CREATED)


    def retrieveDetail(self, request, pk):
        queryset = UserInfo.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def updateUser(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet, data=request.data,partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def deleteUser(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response("deleted",status=status.HTTP_200_OK)
















# class CustomPageNumberPagination(PageNumberPagination):
#     page_size_query_param = 'limit'
#
# class Check(viewsets.ModelViewSet):
#     queryset = UserInfo.objects.all()
#     serializer_class = UserSerializer
#     pagination_class = CustomPageNumberPagination
#
#
#
#     def list(self, request):
#
#
#
#         name = request.GET.get('name',None)
#         q_object=Q()
#         if name is not None:
#             q_object |= Q(first_name__icontains=name)
#             q_object |= Q(last_name__icontains=name)
#         userObjects = UserInfo.objects.filter(q_object)
#         serializedData=UserSerializer(userObjects,many=True)
#         paginator = CustomPageNumberPagination()
#         data = paginator.paginate_queryset(serializedData.data, request)
#
#         return Response(data)







