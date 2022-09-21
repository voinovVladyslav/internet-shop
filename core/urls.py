from django.urls import path

from core import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('catalog/', views.ItemListView.as_view(), name='catalog'),
]
