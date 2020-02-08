from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('2019/', views.classify_2019, name='classify_2019'),
    path('2019/<movie_type>/', views.year_data_2019, name='2019_year_data'),
    path('2018/', views.classify_2018, name='classify_2018'),
    path('2018/<movie_type>/', views.year_data_2018, name='2018_year_data'),
    # path('test/', views.test, name='test'),
]