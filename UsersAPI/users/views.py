from django.shortcuts import render
from .models import UsersData
from rest_framework.views import APIView
from django.http import Http404
from .serializers import UsersSerializer,CreateUsersSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class Users(APIView):
    """
    Retrieve user list
    """

    def get_object(self, request):
        try:
            return  UsersData.objects.get(user=request.user)
        except UsersData.DoesNotExist:
            raise Http404

    def get(self, request, **kwargs):
        """
        search username
        :param request:
        :param kwargs: ?username=kush
        :return:
        """
        username = request.query_params.get("username", None)
        user_profile_obj = UsersData.objects.filter(status__in=["Active", "Inactive"]).order_by("id")
        if username is not None:
            user_profile_obj = user_profile_obj.filter(full_name__contains=username)
        serializer = UsersSerializer(user_profile_obj, many=True)
        return Response(serializer.data)

    def post(self,request):
        """
        :param request:{"full_name":"kush bhargava","emp_code":2,"email":"bhargavakush93@gmail.com"}
        :return: return user data
        """
        serializer = CreateUsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
