from django.urls import path
from . import views
from jewelry.views import details

urlpatterns=[
    path('all', views.clothes, name='allclothes'),
    path('<str:category>', views.category, name='category'),
    path('', views.search, name='search'),
    path('<int:pk>/', views.show, name='detailC')
]