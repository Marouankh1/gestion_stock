from django.urls import path
from .views import product_list, product_create, product_update, product_delete, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add/', product_create, name='product_add'),
    path('update/<int:pk>/', product_update, name='product_update'),
    path('delete/<int:pk>/', product_delete, name='product_delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]