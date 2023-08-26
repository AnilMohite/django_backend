from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data={
        'name':'Anil Mohite',
        'role':'Admin'
    }
    return render(request,'home.html',context=data)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
]
