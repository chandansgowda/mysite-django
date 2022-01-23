from django.contrib import admin

from blog.models import Author, Post, Tags

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ("title","author", "slug", "date")
    list_filter = ("author", "tags", "date")

admin.site.register(Post,PostAdmin)
admin.site.register(Tags)
admin.site.register(Author)