from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
# 定义home方法，用来做为首页
def home(req):
    Url = 'http://' + req.get_host() + req.path
   
    text = '你好：游客！|<a href="../login/">登录</a>'
    username = req.COOKIES.get('username', '')
    if username != '':
        text = '你好：{0} | <a href="../login/logout/">注销</a>'.format(username)
    
    res = HttpResponse(text) 
    res.set_cookie('jump_url', Url, 3600)
    
    return  res  # 先试试输出效果
    
    # req.set_cookie('host',Url,3600)
