'''
product urls
'''
from django.urls import path

from product import views

urlpatterns = [
    path('create/', views.product_create, name='create'),
    path('delete/', views.product_delete, name='delete_product'),
    path('detail/<int:pk>', views.product_detail),
    path('', views.product_list, name='home'),
    path('update/<int:pk>/', views.product_update, name='update_product'),
    path('<int:pk>/purchase/', views.purchased_view, name='purchased'),
    path('purchasedhistory/',views.product_order),

]
