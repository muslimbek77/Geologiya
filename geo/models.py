from django.db import models
from ckeditor.fields import RichTextField

#yangiliklar 
class CategoryYangiliklar(models.Model):
    title = models.CharField(max_length=225)
    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title

class Yangiliklar(models.Model):
    category = models.ForeignKey(CategoryYangiliklar, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title
    


#Elonlar
class CategoryElonlar(models.Model):
    title = models.CharField(max_length=225)
    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title

class Elonlar(models.Model):
    category = models.ForeignKey(CategoryElonlar, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title