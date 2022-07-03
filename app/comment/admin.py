from django.contrib import admin

from comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    class Meta:
        model = Comment

    list_display = ['id', 'user', 'movie', 'value']
    list_display_links = ['id', 'user']


admin.site.register(Comment, CommentAdmin)
