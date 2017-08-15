"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

app_name = 'itake'

urlpatterns = [
    #url for homepage
    url(r'^$',views.index,name="index"),
    #url for login
    url(r'^login/$', views.login1, name = "login"),

    #url for product pages
    url(r'^product/$',views.productList.as_view(),name="productList"),
    url(r'^product/add/$', views.productCreate.as_view(), name = "productCreate"),
    url(r'^product/update/(?P<product_id>[0-9]+)/$', views.productUpdate, name="productUpdate"),
    url(r'^product/(?P<product_id>[0-9]+)/$',views.productDetails, name="productDetails"),
    url(r'^product/delete/(?P<product_id>[0-9]+)/$', views.productDelete, name = "productDelete"),

    #url for vendor pages
    url(r'^vendor/$',views.vendorList.as_view(),name="vendorList"),
    url(r'^vendor/(?P<vendor_id>[0-9]+)/$',views.vendorDetails, name="vendorDetails"),
    url(r'^vendor/add/$', views.vendorCreate.as_view(), name="vendorCreate"),

    #url for order pages
    url(r'^order/$',views.orderList.as_view(),name="orderList"),
    url(r'^order/(?P<order_id>[0-9]+)/$',views.orderDetails, name="orderDetails"),
    url(r'^order/add/$', views.orderCreate.as_view(), name = "orderCreate"),

]

urlpatterns += staticfiles_urlpatterns()