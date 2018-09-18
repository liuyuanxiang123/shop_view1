from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from apps.home.models import *


def index(request):
    #导航菜单数据
    navigations=Navigation.objects.all()
    # 分类菜单的数据
    categorys=Category.objects.all()
    for categroy in categorys:
        categroy.subs=categroy.submenu_set.all()
        for sub in categroy.subs:
            sub.sub2=sub.submenu2_set.all()
    #轮播图数据
    banners=Banner.objects.all()

    return render(request,'index.html',{'categorys':categorys, 'navigations':navigations,'banners':banners})