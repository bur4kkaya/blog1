from django.contrib import admin
# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'publishing_date']
    list_display_links = ['title', 'publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title', 'content']
    #list_editable = ['title']

    class Meta:
        model=Post


admin.site.register(Post, PostAdmin)
