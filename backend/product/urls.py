from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_home),
    path("product-detail/<int:pk>/", views.ProductDetailAPIView.as_view()),
    
]