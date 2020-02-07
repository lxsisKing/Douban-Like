from django.db import models


# Create your models here.


class MovieData2019(models.Model):
    # 创建相关数据
    movie_name = models.CharField(max_length=128, verbose_name='电影名')
    movie_orig_name = models.CharField(max_length=128, verbose_name='别名')
    movie_rate = models.FloatField(default=0, verbose_name='得分')
    movie_url = models.CharField(max_length=128, verbose_name='相关豆瓣地址')
    movie_type = models.CharField(max_length=128, verbose_name='所属类型')
    c_time = models.DateTimeField('添加时间', auto_now_add=True)

    def __str__(self):
        return self.movie_name

    class Meta:
        ordering = ['c_time']  # 定义排序方法
        db_table = '2019MovieData'  # 定义表名
        verbose_name = '2019年度榜单'  # 定义在admin中直观易读的名字
        verbose_name_plural = '2019年度榜单'  # 复数


class MovieData2018(models.Model):
    movie_name = models.CharField(max_length=128, verbose_name='电影名')
    movie_orig_name = models.CharField(max_length=128, verbose_name='别名')
    movie_rate = models.FloatField(default=0, verbose_name='得分')
    movie_url = models.CharField(max_length=128, verbose_name='相关豆瓣地址')
    movie_type = models.CharField(max_length=128, verbose_name='所属类型')
    c_time = models.DateTimeField('添加时间', auto_now_add=True)

    def __str__(self):
        return self.movie_name

    class Meta:
        ordering = ['c_time']
        db_table = '2018MovieData'
        verbose_name = '2018年度榜单'
        verbose_name_plural = '2018年度榜单'

# class MovieType(models.Model):
#     movie_type = models.CharField(max_length=128, primary_key=True, unique=True, verbose_name='电影类别')
#     c_time = models.DateTimeField('添加时间', auto_now_add=True)
#
#     def __str__(self):
#         return self.movie_type
#
#     class Meta:
#         ordering = ['c_time']
#         db_table = 'MovieType'
#         verbose_name = '电影类别'
#         verbose_name_plural = '电影类别'
