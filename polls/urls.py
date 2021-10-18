from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="index"),
    path('test', views.test, name="index")
]