# -*- coding:utf-8 -*-
from django.urls import path
from django.views.static import serve
from . import views
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# 将url传入view.index模块中， index类别名name
#urlpatterns = [path(r'', views.index, name='index'), ]
from django.views.generic.base import RedirectView

urlpatterns = [path(r'', views.index, name='index'),
	path(r'mysite/blog/templates/blog/', views.show_picture, name='show_picture'),url(r'^favicon.ico$',RedirectView.as_view(url=r'/static/favicon.ico',permanent=True)),
	#path('show/', views.showimg, name='photos'),path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 这句话是用来指定和映射静态文件的路径