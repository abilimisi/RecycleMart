from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
path('', views.product_list, name='product_list'),
path('signup/', views.signup_view, name='signup'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('product/<int:pk>/', views.product_detail, name='product_detail'),
path('product/add/', views.product_add, name='product_add'),
path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
]