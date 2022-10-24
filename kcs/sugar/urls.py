from . import views

from django.urls import path

urlpatterns = [
    # url for filter
    path('', views.HomePageView.as_view(), name='home-page'),


]