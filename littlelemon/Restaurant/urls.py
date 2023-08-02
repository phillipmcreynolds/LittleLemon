from django.urls import path, include, re_path
from django.contrib import admin
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/items/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]