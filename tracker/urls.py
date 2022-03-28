from django.urls import path

from tracker import views

urlpatterns = [
    path('', views.homepage),
    path('login', views.signin),
    path('registration', views.register),
    path('dashboard', views.dashboard),
    path('logout', views.sign_out)
]
