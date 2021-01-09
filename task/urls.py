from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'2', TaskViewSet)

urlpatterns = [
	path('', include(router.urls))
]