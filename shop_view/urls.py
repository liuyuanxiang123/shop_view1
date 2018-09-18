from django.conf.urls import url,include
from django.contrib import admin

from home import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('account/',include('account.urls')),
    url('cart/',include('cart.urls')),
    url('home',include('home.urls')),
    url('order',include('order.urls')),
    url('pay',include('pay.urls')),
    url('shop',include('shop_detail.urls')),
    url('cate',include('cate.urls')),
    url('^$',views.index)
]
