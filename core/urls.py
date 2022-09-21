from django.urls import path

from core import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('catalog/', views.ItemListView.as_view(), name='catalog'),
    path('item/<str:pk>/', views.ItemDetailView.as_view(), name='item'),
]
