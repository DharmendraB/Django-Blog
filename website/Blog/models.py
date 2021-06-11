from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Category(models.Model):
    cat_name = models.CharField(max_length=60)    
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=60)    
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name
        
class BlogPost(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    post_cat = models.ForeignKey(to=Category, on_delete=models.SET_NULL,blank=True, null=True)
    post_tag = models.ForeignKey(to=Tag, on_delete=models.SET_NULL,blank=True, null=True)
    # pip install pillow==6.0.0 --user
    #python -m pip install Pillow
    image = models.ImageField(upload_to="media/blog/images", default="")
    uploaded_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.title

class PostCommet(models.Model):
    post = models.ForeignKey(to=BlogPost, on_delete=CASCADE)
    msg = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)   
    commited_by = models.ForeignKey(to=User, on_delete=CASCADE) 
    flag = models.CharField(max_length=20, null=True, blank=True, choices=(("Racist","Racist"),("Abbusing","Abbusing")))  
    def __str__(self):
        return "%s" % self.msg