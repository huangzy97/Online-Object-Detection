# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from .models import user,IMG
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect 

from media.research.object_detection import  object_detection_spyder_test as ods



# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(required=False)
    headImg = forms.ImageField(required=False)
@csrf_exempt
def index(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            #print(request.FILES)
            #获取表单信息request.FILES是个字典
            User = user(headImg=request.FILES['file'])
            #保存在服务器
            User.save()
            global name
            name = str(User.headImg).split('/')[-1]
            ods.main(name)
            return HttpResponse('识别成功,请查看识别结果!')

    return render(request, 'blog/index.html')
	
def show_picture(request):
    import os
    filename='../media/research/object_detection/test_images/'
    ext = os.path.splitext(name)[1]
    name_result = os.path.splitext(name)[0]
    context={'name':filename+name_result+'_result'+ext}
    print(context)
    return render(request,'blog/Welcome.html',context)
def showimg(request):
    imgs = models.mypicture.objects.all() # 查询到数据库所有图片
    # 创建一个字典来存储这些图片信息
    content = {
        'imgs': imgs
    }
    # 打印一下这些图片信息
    for i in imgs:
        # 输出一下信息内容
        print(i.photo)
    # 最后返回一下我们的展示网页，动态图片数据展示放进去
    return render(request, 'bbb.html', content)	
	
def hello(request):
    IMG.objects.filter(name='bg')
    img = IMG.objects.all()
    return render(request, 'blog/Welcome.html',{'img':img})


#https://blog.csdn.net/W1948730080/article/details/82184444
# Create your views here.
# def index(request):
#     return render(request, 'blog/index.html')