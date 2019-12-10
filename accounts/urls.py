from django.urls import path
from . import views

# We want the URL's to look like /listings/<id>
urlpatterns = [
        path('login', views.login, name='login'),
        path('register', views.register, name='register'),
        path('logout', views.logout, name='logout'),
        path('dashboard', views.dashboard, name='dashboard'),
]