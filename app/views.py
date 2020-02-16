from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from  .serializers import UserSerializer
from rest_framework import status
from django.http import Http404
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action
from django.db.models import  Q
from rest_framework.generics import ListAPIView
# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination






class UserViewSet(viewsets.ViewSet):
    queryset = UserInfo.objects.all()
    serializer = UserSerializer

    # def get_paginated_response(self, data):
    #     return Response({
    #         'links': {
    #             'next': self.get_next_link(),
    #             'previous': self.get_previous_link()
    #         },
    #         'count': self.page.paginator.count,
    #         'page_size': self.page_size,
    #         'results': data
    #     })
    def get_object(self, pk):
        try:
            return UserInfo.objects.get(pk=pk)
        except UserInfo.DoesNotExist:
            raise Http404("user does not exist")

    @action(detail=False, methods=['get'], url_path='users')
    def listUsers(self, request, *args, **kwargs):
        queryset = UserInfo.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='users1')
    def createUser(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("user created",status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_path='userDetail')
    def retrieveDetail(self, request, pk):
        queryset = UserInfo.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


    @action(detail=False,methods=['get'],url_path='users1')
    def userDetail(self,request):

        name=request.GET.get('name')
        user=UserInfo.objects.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        serializer=UserSerializer(user,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)


    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response("deleted",status=status.HTTP_200_OK)



class Check(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer
    #pagination_class = PageNumberPagination

    def list(self, request):
        serializer = self.get_serializer_class()
        paginator = LimitOffsetPagination()
        paginator.default_limit = 15
        paginator.limit = paginator.get_limit(request)
        paginator.offset = paginator.get_offset(request)
        feeds = paginator.paginate_queryset(UserInfo.objects.all(), request)
        return Response(
            data={
                'feeds': serializer(feeds, many=True).data,
                'limit': paginator.limit,
                'offset': paginator.offset,
                'overall_count': paginator.count
            }
        )
        # data = [
        #     {"id": 1},
        #     {"id": 2},
        # ]
        # data=self.get_queryset()
        # #data=UserSerializer(data,many=True)
        # #print(data)
        # paginator = PageNumberPagination()
        # page = paginator.paginate_queryset(data, request)
        # print(page)
        # print("checking the work")
        # page=UserSerializer(page,many=True)
        # #print*
        # #print*
        # if page is not None:
        #     return paginator.get_paginated_response(page)
        #
        # return Response(data)






