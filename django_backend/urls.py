from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

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
    path('api/', include('blogs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
