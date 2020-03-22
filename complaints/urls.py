from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.test, name='home'),
   # path('/', views.complaints_form),
    path('list/', views.complaints_records)
]
