from django.shortcuts import render, get_object_or_404
from . import models

from django.http import HttpResponse


# Create your views here.


def data(request):
    pass
    return render(request, 'data_integration/data.html')


def year_data_2019(request, movie_type):
    # 获取数据库中对应表的数据
    year_rank_data = models.MovieData2019.objects.filter(movie_type__exact=movie_type)
    # 将数据传递到H5页面并渲染
    return render(request, 'data_integration/get_2019year_data.html', locals())


def year_data_2018(request, movie_type):
    year_rank_data = models.MovieData2018.objects.filter(movie_type__exact=movie_type)
    return render(request, 'data_integration/get_2018year_data.html', locals())


# def test(request):
#     year_rank_data = models.MovieData2019.objects.all()
#     return render(request, 'data_integration/index.html', locals())


def classify_2019(request):
    classify_data = models.MovieData2019.objects.values('movie_type')
    classify_data_2019 = []
    for movie_type in classify_data:
        if movie_type['movie_type'] not in classify_data_2019:
            classify_data_2019.append(movie_type['movie_type'])
    return render(request, 'data_integration/classify_2019.html', {'classify_data_2019_dic': classify_data_2019})


def classify_2018(request):
    classify_data = models.MovieData2018.objects.values('movie_type')
    classify_data_2018 = []
    for movie_type in classify_data:
        if movie_type['movie_type'] not in classify_data_2018:
            classify_data_2018.append(movie_type['movie_type'])
    return render(request, 'data_integration/classify_2018.html', {'classify_data_2018_dic': classify_data_2018})
