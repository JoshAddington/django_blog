from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
        model = Comment
        extra = 3


class PostAdmin(admin.ModelAdmin):
        fieldsets = [
                (None, {'fields': ['author', 'title', 'project', 'text']}),
                ('Date Information', {'fields': ['created_date', 'published_date']}),
                ('Comments', {'fields': ['post.comment_set']}),
        ]

        inlines = [CommentInline]
        list_display = ('title', 'project', 'created_date', 'published_date')


class CommentAdmin(admin.ModelAdmin):
        fieldsets = [
                (None, {'fields': ['author', 'post', 'text', 'posted_date']}),
        ]

        list_display = ('post', 'author', 'text')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
