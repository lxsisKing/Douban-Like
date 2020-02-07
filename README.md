# Douban-Like

结合**Django**与**Scrapy**获取豆瓣相关感兴趣的数据进行优化处理后显示。

### Scrapy部分

Scrapy与Django的结合使用到了scrapy-djangoitem扩展。

相关地址：https://pypi.org/project/scrapy-djangoitem/
  
**安装**  

```shell
pip install scrapy-djangoitem
```

**使用**  

 ```python
 from scrapy_djangoitem import DjangoItem
 ```
 
 ### Django部分
 
 连接数据库需要安装mysqlclient
 
 相关地址：https://pypi.org/project/mysqlclient/
 
 **安装**
```shell
pip install mysqlclient
````

**更改setting.py设置文件**

```python
import pymysql
pymysql.install_as_MySQLdb()

...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '填入自己创建的数据库名',
        'USER': '数据库用户',
        'PASSWORD': '连接数据库密码',
        'HOST': '相关IP',
        'PORT': '端口（MySQL为3306）',
    }
}
```

### 前端

由于自己前端能力较弱，同时审美设计能力不够。所以前端相关代码均使用现成素材进行二次开发。

相关界面显示如下。

![alt 第一张图](https://github.com/lxsisKing/Douban-Like/blob/master/project_image/1.jpg)
    
 
 
 
