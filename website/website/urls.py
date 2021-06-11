from django.contrib import admin
from django.urls import path,include
admin.site.site_header = 'Best Blog'
admin.site.index_title = 'Best Blog Admin Area' 
from django.conf import settings
from django.conf.urls.static import static
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Blog.urls')),
    path('blog/',include('Blog.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)