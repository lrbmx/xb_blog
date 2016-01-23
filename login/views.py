from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from login.models import User


# Create your views here.
# 表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：', max_length=100)
    password = forms.CharField(label='密码：', widget=forms.PasswordInput())
    
# 注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 添加到数据库
            User.objects.create(UserName=username, PassWord=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf':uf}, context_instance=RequestContext(req))


# 登录
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = User.objects.filter(UserName__exact=username, PassWord__exact=password)
            if user:
                response = HttpResponseRedirect('/login/index/')
                # 将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 3600)
                return response
            else:
                return HttpResponseRedirect('/login/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf':uf})

# 登陆成功
def index(req):
    #jump_url = req.COOKIES.get('jump_url')
    username = req.COOKIES.get('username')
    html = render_to_response('index.html' , {'username':username})
    # html = render_to_response(html ,{'jump_url':jump_url})
    return html

# 退出
def logout(req):
    response = render_to_response('loginout.html')
    response.delete_cookie('username')
    return response
