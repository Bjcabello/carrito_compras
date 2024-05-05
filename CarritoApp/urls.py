from django.urls import path
from . import views


app_name = "CarritoApp"

urlpatterns = [
    path('add/<int:producto_id>/', views.add_product, name="add"),
    path('delete/<int:producto_id>/', views.delete_product, name="delete"),
    path('subtract/<int:producto_id>/', views.subtract_product, name="subtract"),
    path('clear/', views.clear_car, name="clear"),
]