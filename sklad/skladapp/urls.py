from django.urls import path
from .views import *
from statisticapp.views import StatisticView

urlpatterns = [
    path('client/', ClientView.as_view(),name='clients'),
    path('client_update/<int:son>/', Client_updateView.as_view(),name='client-update'),
    path('product/', ProductView.as_view(),name='stats'),
    path('product/', ProductView.as_view(),name='goods'),
    path('product_update/<int:son>/', Product_updateView.as_view(),name='product-update'),
    # path('product_update/<int:son>/', Product_update,name='product-update'),
    path('register', RegisterView.as_view(),name='register'),
    path('logout/',Logout,name='logout'),
    path('', BulimlarView.as_view(),name='bolim'),
]