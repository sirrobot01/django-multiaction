from django.shortcuts import render
from multiaction import BaseAction, BaseConnector
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.http import JsonResponse
# Create your views here.

class UsersActions(BaseAction):
    
    def is_permitted(self, request, *args, **kwargs):
        return True
    
    def create_user(self, request, *args, **kwargs) -> JsonResponse:
        username = request.GET.get('username')
        fname = request.GET.get('fname')
        lname = request.GET.get('lname')
        user = User.objects.create(username=username, first_name=fname, last_name=lname)
        
        return JsonResponse(data={"id": user.id, "username": user.username, "first_name": user.first_name}, status=201)
    
    def get_user(self, request, *args, **kwargs) -> JsonResponse:
        user_id = request.GET.get('user_id')
        user = User.objects.get(id=user_id)
        return JsonResponse(data={"id": user.id, "username": user.username, "first_name": user.first_name}, status=200)
    
    def get_users(self, request, *args, **kwargs) -> JsonResponse:
        data = User.objects.values('id', 'username', 'first_name')
        
        return JsonResponse(data=list(data), status=200, safe=False)


class MultiActionView(BaseConnector, APIView):
    actions = {
        'user': UsersActions
    }
