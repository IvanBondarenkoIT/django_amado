from django.urls import path
from . import views

app_name = 'shop'


urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:id>/', views._filter, name='_filter'),
]