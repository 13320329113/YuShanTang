"""pydcdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import myadmin, wxs
from . import dcapi

urlpatterns = [
    path('', myadmin.hello),
    path('admin/', admin.site.urls),
    path('hello/', myadmin.hello),
    path('test/', myadmin.test),
    path('testdata/', myadmin.testdata),
    path('foodadd/', myadmin.foodadd),
    path('foodaddpost/', myadmin.foodaddpost),
    path('foodlist/', myadmin.foodlist),
    path('foodedit/', myadmin.foodedit),
    path('foodeditpost/', myadmin.foodeditpost),
    path('fooddelete/', myadmin.fooddelete),
    path('drinkadd/', myadmin.drinkadd),
    path('drinkaddpost/', myadmin.drinkaddpost),
    path('drinklist/', myadmin.drinklist),
    path('drinkedit/', myadmin.drinkedit),
    path('drinkeditpost/', myadmin.drinkeditpost),
    path('drinkdelete/', myadmin.drinkdelete),
    path('orderlist/', myadmin.orderlist),
    path('orderdelete/', myadmin.orderdelete),
    path('orderview/', myadmin.orderview),
    path('login/', myadmin.login),
    path('loginpost/', myadmin.loginpost),
    path('dcapi/reg', dcapi.reg),
    path('dcapi/login', dcapi.login),
    path('dcapi/getfoodlist', dcapi.getfoodlist),
    path('dcapi/getfoodlistbyrandom', dcapi.getfoodlistbyrandom),
    path('dcapi/getfoodbyid', dcapi.getfoodbyid),
    path('dcapi/addtocar', dcapi.addtocar),
    path('dcapi/getcarlist', dcapi.getcarlist),
    path('dcapi/changecarnum', dcapi.changecarnum),
    path('dcapi/deleteitembyid', dcapi.deleteitembyid),
    path('dcapi/saveorder', dcapi.saveorder),
    path('dcapi/getorderlist', dcapi.getorderlist),
    path('dcapi/saveliuyan', dcapi.saveliuyan),
    path('dcapi/register', dcapi.register),
    path('dcapi/getdrinklist', dcapi.getdrinklist),
    path('cooklistadd/', wxs.cooklistadd),
    path('cookeraddpost/', wxs.cookeraddpost),
    path('cooklist/', wxs.cooklist),
    path('cookedit/', wxs.cookedit),
    path('cookeditpost/', wxs.cookeditpost),
    path('cookdelete/', wxs.cookdelete),
    path('dcapi/getcooklist', dcapi.getcooklist),
    path('lunbosetting/', myadmin.lunbosetting),
    path('privateroom/', myadmin.privateroom),
    path('lunbopost/', myadmin.lunbopost),
    path('roompost/', myadmin.roompost),
    path('dcapi/getroomlist', dcapi.getroomlist),
    path('dcapi/getlunbolistbyrandom', dcapi.getlunbolistbyrandom),
    path('dcapi/getdatalistbyrandom', dcapi.getdatalistbyrandom),


]
