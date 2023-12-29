from django.contrib import admin
from .models import Comment, Activity, Status

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    model = Comment

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    model = Activity

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    model = Status


# admin.register(Status, StatusAdmin)

admin.register(Comment, CommentAdmin)


