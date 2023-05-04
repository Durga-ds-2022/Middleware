from django.urls import path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('user', UserView)


app_name = 'User_account'


urlpatterns = [
    path('', include(router.urls))
]