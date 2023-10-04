from django.contrib import admin
from blog1.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "pub_date")
    #當你訪問管理站點並查看 Post 模型時，將會按照 list_display 屬性指定的順序和字段顯示數據


admin.site.register(Post, PostAdmin) 
