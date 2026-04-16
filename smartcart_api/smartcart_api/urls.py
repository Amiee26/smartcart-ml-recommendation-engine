from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [

    path('', views.home),
    path('admin/', admin.site.urls),
    path('api/recommend/<str:product_name>/', views.recommend_products),
    path('api/suggest/', views.suggest_products),
    path('api/top-products/', views.top_products),

]
