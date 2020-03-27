from django.urls import path, include
from . import views

urlpatterns = [
    
   # path('', views.test, name='home'),
    path('', views.index, name='Home'),
    path('list/', views.complaints_records, name='All records'),
    path('forms/', views.complaints_form1, name='complaint form'),
    path('csv/', views.getfile, name='csv file download')
    
]
