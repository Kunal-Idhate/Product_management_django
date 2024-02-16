from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.index, name="home"),
    path('add', views.AddProduct, name="add"),
    path('adduser', views.AddUser, name="adduser"),
    path('update/<str:id>', views.UpdateProduct, name="update"),
    path('delete/<str:id>', views.DeleteProduct, name="Delete"),
    path('users', views.Users, name="users"),
    path('updateuser/<str:id>', views.UpdateUser, name="updateUser"),
    path('deleteuser/<str:id>', views.DeleteUser, name="deleteUSer"),
    path('search/product', views.SearchProduct, name="searchProduct"),

    
]
