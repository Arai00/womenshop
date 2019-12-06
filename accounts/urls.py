from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views as not_based_view

urlpatterns=[
    path('registration', not_based_view.register.as_view(), name='registration'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout')

]
