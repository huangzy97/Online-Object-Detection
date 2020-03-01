from django.db import models
from django.contrib.auth.models import User
#
# # Create your models here.
#
# # 新建一个Category 分类数据库表, key为name，数据类型char，值的最大长度150
# class Category(models.Model):
#     name = models.CharField(max_length=150)
#
# # 标签数据库
# class Tag(models.Model):
#     name = models.CharField(max_length=150)
#
#
# class Post(models.Model):
#     # 文章标题较短 char字符
#     title = models.CharField(max_length=150)
#     # 内容较多，用text
#     body = models.TextField()
#     created_time = models.DateTimeField()
#     modified_time = models.DateTimeField()
#     # 摘要可以为空
#     excerpt = models.CharField(max_length=150, blank=True)
#
#     # 数据库表间的联系，ForeignKey一对多，ManyToManyField多对多
#     category = models.ForeignKey('Category',on_delete=models.CASCADE)
#     tags = models.ManyToManyField(Tag, blank=True)
#     author = models.ForeignKey(User,on_delete=models.CASCADE)
from system.storage import ImageStorage
class user(models.Model):
    headImg = models.ImageField(upload_to='research/object_detection/test_images/',storage=ImageStorage())
    username = models.CharField(max_length=100)
    def __str__(self):
        return self.headImg
#pic=models.ImageField(upload_to='img/%Y/%m/%d',storage=ImageStorage())  #如果上传文件可以将ImageField换为FileField
    #headImg = models.ImageField(upload_to='research/object_detection/test_images/')
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __unicode__(self):
    # 在Python3中使用 def __str__(self):
        return self.name

class IMG(models.Model):
    img = models.ImageField(upload_to='research/object_detection/test_images/')
    name = models.CharField(max_length=20)
    def __str__(self):
    # 在Python3中使用 def __str__(self):
        return self.name 
	#headImg = models.ImageField(upload_to='research/object_detection/test_images/%Y/%m/%d',storage=ImageStorage())
	
	
	
	
	
