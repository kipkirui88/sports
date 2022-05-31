from django.urls import path
from . import views
from .views import predictions

urlpatterns = [
    path('', views.index, name='index'),
    path('predictions/', predictions.as_view(), name='predictions')
]