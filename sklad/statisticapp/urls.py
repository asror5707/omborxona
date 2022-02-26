from django.urls import path
from statisticapp.views import StatisticView

urlpatterns = [
    path('statis/', StatisticView.as_view(),name='statis'),
]