
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import routers
from .views import BlogViewSet

def index(request):
    return HttpResponse("<h1 style='text-align:center'>Blog App<h1>")

router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet, basename='blog')
urlpatterns = [
    path('', index),
    path('', include(router.urls))
]
