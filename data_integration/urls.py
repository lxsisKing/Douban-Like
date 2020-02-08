from django.urls import path
from . import views

urlpatterns = [
    # name为别名，作用为方便在模板中后续更换url地址，去除硬编码
    path('', views.index, name='index'),
    path('2019/', views.classify_2019, name='classify_2019'),
    # 使用path转换器。没有指定的话默认为str，匹配任意非空字符串
    path('2019/<movie_type>/', views.year_data_2019, name='2019_year_data'),
    path('2018/', views.classify_2018, name='classify_2018'),
    path('2018/<movie_type>/', views.year_data_2018, name='2018_year_data'),
    # path('test/', views.test, name='test'),
]