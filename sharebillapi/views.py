from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.contrib.auth.models import User
from sharebillapi.forms import *
from sharebillapi.api_errors import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

import json

class LoginView(APIView):
    response = {}

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        self.response['error'] = api_errors.SUCCESS
                        self.response['error_message'] =api_errors_message.SUCCESS
                    else:
                        self.response['error'] = api_errors.ACCOUNT_DIABLED
                        self.response['error_message'] =api_errors_message.ACCOUNT_DIABLED
                else:
                    self.response['error'] = api_errors.USER_NOT_FOUND
                    self.response['error_message'] =api_errors_message.USER_NOT_FOUND
            except Exception as e:
                self.response['error'] = api_errors.UNEXPECTED_ERROR
                self.response['error_message'] = api_errors_message.UNEXPECTED_ERROR + 'error: ' + str(e)
        else:
            self.response['error'] = api_errors.FORM_INVALID
            self.response['error_message'] =api_errors_message.FORM_INVALID
        return HttpResponse(json.dumps(self.response), content_type="application/json")
