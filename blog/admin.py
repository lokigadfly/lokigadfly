from django.contrib import admin

# Register your models here.
from blog.models import Article, Category, Tag,Link,Product,Board

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Link)
admin.site.register(Product)
admin.site.register(Board)