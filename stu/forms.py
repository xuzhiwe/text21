# #coding=utf-8
# from django import forms
# from .models import *
#
#
# class LoginForm(forms.Form):
#     sname = forms.CharField(max_length=30,label=u'姓名：')
#     spwd = forms.CharField(label=u'密码：')
#
# class ClazzForm(forms.ModelForm):
#     class Meta:
#         model = Clazz
#         fields = ('cname',)
#
# class StuForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput,max_length=30,label=u'密码1：')
#     password2 = forms.CharField(widget=forms.PasswordInput, max_length=30,label=u'密码2：')
#     class Meta:
#         model =  Stu
#         fields = ('sname',)
#
#     def clean_password2(self):
#         data = self.cleaned_data
#         if data['password'] != data['password2']:
#             self.errors['password2']=['密码不一致']
#         return data['password2']
