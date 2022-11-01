from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import ClientModel


class HomePageView(View):

    def get(self, request):
        return render(request, 'sugar/home.html')
    def post(self ,request):
        client = ClientModel()
        client.name =  request.POST.get('name')
        client.number = request.POST.get('number')
        client.save()
        return render(request, 'sugar/registred.html')