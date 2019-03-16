# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from .forms import *
from .models import *
# Create your views here.




# class IndexView(View):
#     def get(self,request):
#         loginform = LoginForm()
#         return render(request,'login.html',{'loginform':loginform})
#
#     def post(self,request):
#         loginform = LoginForm(request.POST)
#         #loginform.is_valid():校验数据是否合法（即 登录验证账号密码是否正确）
#         if loginform.is_valid():
#             data = loginform.cleaned_data
#             user = authenticate(username=data['sname'],password=data['spwd'])
#             if user:
#                 #将用户信息存放至session
#                 login(request,user)
#                 return HttpResponse('登陆成功！')
#         return HttpResponse('登录失败！')
#
#
# class RegisterView(View):
#     def get(self,request):
#         #创建表单对象
#         clsForm = ClazzForm()
#         stuForm = StuForm()
#         return render(request,'register.html',{'clsForm':clsForm,'stuForm':StuForm})
#
#     def post(self,request):
#         #创建表单对象
#         clsForm = ClazzForm(request.POST)
#         stuForm = StuForm(request.POST)
#
#         #验证表单数据是否合法
#         if clsForm.is_valid()*stuForm.is_valid():
#             cls = clsForm.save()
#             stu =  stuForm.save(commit=False)
#             stu.clazz = cls
#             stu.password = stuForm.clean_password2()
#             stu.save()
#             return HttpResponse('注册成功！')
#         return render(request,'register.html',{'clsForm':clsForm,'stuForm':StuForm})
#

def onlyView(request):
    return render(request,'only.html')


def existView(request):
    #接受请求参数
    uname = request.GET.get('uname','')
    #判断数据库中是否存在
    stuList = Student.objects.filter(sname=uname)
    if stuList:
        return JsonResponse({'flag':True})
    return JsonResponse({'flag':False})
    return None