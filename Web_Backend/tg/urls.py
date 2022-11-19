from django.urls import path
from . import views
urlpatterns = [
    # path('', views.index),  
    path('',views.tgmap),  
    path('products/',views.products), #<int:uid>/<str:sid>/     
]
