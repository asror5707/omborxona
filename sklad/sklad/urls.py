
from django.contrib import admin
from django.urls import path, include
from skladapp.views import *
from statisticapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bolim/',include('skladapp.urls')),
    path('bolim/',include('statisticapp.urls')),
    path('', IndexView.as_view(),name='login'),


]
