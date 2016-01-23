from blog.models import BlogPost
from blog.models import BlogType
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render,render_to_response

from django.template import loader, Context


# Create your views here.


def index(request):
    print(request.GET.get('name'))
    page = request.GET.get('page', 1)
    print('page:' + str( page))
    TempName = "index.html"
    Show_len = 3
    blog_list = BlogPost.objects.all().order_by("-time_stamp")
    i = 0
    type_list=[]
    while i < len(blog_list):
        type_id = blog_list[i].blog_type_id
        new = NewObj(blog_list[i])
        new.type_name(get_type_name(type_id))
        type_list.append([new])
        i += 1
    
    y = Paginator(type_list, Show_len)
    t = loader.get_template(TempName)    
    yy = y.page(int(page))
    c = Context({'posts':yy, 'blog_len':str(y.count)})
    return HttpResponse(t.render(c))

def look(request,view):
    TempName = "view.html"
    blog = BlogPost.objects.get(id=int(view))
    type_name = BlogType.objects.get(id=blog.blog_type_id)
    #t = loader.get_template(TempName)
    conn = {'posts':blog,'type':type_name}
    html = render_to_response(TempName , conn)
    return html




def get_type_name(type_id):
    type_name = BlogType.objects.get(id=int(type_id))
    return type_name.type_name

def get_blog_title(title_id):
    title = BlogPost.objects.get(id=int(id))
    return str(title)
    
class NewObj(BlogPost):  
    def __init__(self,BlogPost): 
        self.id=BlogPost.id
        self.title=BlogPost.title
        self.time=BlogPost.time_stamp
        self.txt=BlogPost.content
    def type_name(self,name):
        self.type_name = name
    
    