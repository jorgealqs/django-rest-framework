from django.contrib import admin
from core.comment.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "body", "created", "updated", "edited",)
    list_filter = ("edited",)
