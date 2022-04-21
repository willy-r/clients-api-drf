from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from clients import views

router = routers.DefaultRouter()
router.register('clients', views.ClientViewSet)

urlpatterns = [
    # API
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
