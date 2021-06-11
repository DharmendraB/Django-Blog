from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import BlogPost,Category,Tag
from django.db.models import Q


def blog(request):
    # return render(request,'onepage/home.html')
    return render(request,'Blog/blog.html')
    
def blogSingle(request):    
    return render(request,'Blog/blog-single.html')

# class BlogView(TemplateView):
#     template_name = 'blog/blog1.html'
#     model = BlogPost
    
 # All Blog posts display code hare
class BlogPostListView(ListView):
    template_name = 'blog/blogpost_list.html'
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        #Get Search textbox values        
        search = self.request.GET.get('uq')  
        #values empty or not check      
        if search != None:            
            BlogPost_list = BlogPost.objects.filter(Q(title__icontains = search)| Q(description__icontains = search)).order_by("-id")                            
        else:
            search =""
            BlogPost_list = BlogPost.objects.order_by("-id")[:10]
        #Right side category display code
        Post_cat = Category.objects.order_by("-id") 
        for p_cat in Post_cat:
            post_count = BlogPost.objects.filter(post_cat = p_cat)
            p_cat.t_count = post_count.count() 
        #Right side Tags display code    
        Post_tag = Tag.objects.order_by("-id") 
        #All Data send for viewtemplate using context
        context["blogpost_list"] = BlogPost_list
        context["post_cat"] = Post_cat
        context["post_tag"] = Post_tag
        return context
    
# Blog post Detail display code here
class BlogPostDetailView(DetailView):
    template_name = 'blog/blogpost_detail.html'
    model = BlogPost
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        BlogPost_list = BlogPost.objects.order_by("-id")[:10]

        #Right side category display code
        Post_cat = Category.objects.order_by("-id") 
        for p_cat in Post_cat:
            post_count = BlogPost.objects.filter(post_cat = p_cat)
            p_cat.t_count = post_count.count()

        #Right side Tag display code    
        Post_tag = Tag.objects.order_by("-id")

        #All Data send for viewtemplate using context
        context["blogpost_list"] = BlogPost_list
        context["post_cat"] = Post_cat
        context["post_tag"] = Post_tag
        return context



    
    

