from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create-recipe'),
    path('edit/<int:pk>/', views.edit, name='edit-recipe'),
    path('delete/<int:pk>/', views.delete, name='delete-recipe'),
    path('details/<int:pk>/', views.details, name='details-recipe'),
]
