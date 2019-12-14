'''
product urls
'''
from django.urls import path

from product import views

urlpatterns = [
    path('create/', views.ProductCreate.as_view(), name='create'),
    path('delete/', views.ProductDelete.as_view(), name='delete_product'),
    path('detail/<int:pk>', views.ProductDetailView.as_view()),
    path('', views.ProductView.as_view(), name='home'),
    path('update/<int:pk>/', views.UpdateProduct.as_view(), name='update_product'),
    path('<int:pk>/purchase/', views.purchased_view, name='purchased'),

]
