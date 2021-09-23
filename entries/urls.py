from django.urls import path

from . import views

# URL шаблоны, связывают URL с отображеними
urlpatterns = [
    path('', views.index_view, name="index"),
    path('create/', views.create_view, name='create'),
    path('edit/<int:pk>/', views.change_view, name='edit'),
    path('delete/<int:pk>/', views.delete_view, name='delete'),
    path('search/', views.search_view, name='search'),
]
