from django.urls import path
from . import views

urlpatterns=[
    path('cart/clothes/<int:pk>', views.cartClothes, name='cartCloth'),
    path('cart/jewelry/<int:pk>', views.cartJew, name='cartJew'),
    path('', views.cartshow, name='cartshow'),
    path('delete', views.delete, name='delete')
]