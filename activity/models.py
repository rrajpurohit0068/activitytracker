from django.db import models

class Status(models.Model):
    title = models.TextField(blank=True, default='')
    desc = models.TextField(blank=True, default='')
    text_color = models.TextField(blank=True, default='')
    background_color = models.TextField(blank=True, default='')
    sr_no = models.IntegerField()


# Create your models here.
class Activity(models.Model):
    title = models.TextField(blank=True, default='')
    desc = models.TextField(blank=True, default='')
    status_id = models.ForeignKey(Status, blank=True,
        null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey('users.MyUser',blank=True,
        null=True, on_delete=models.SET_NULL) 
    priority = models.IntegerField()
    def __str__(self):
        return self.title


class Comment(models.Model):
    activity_id = models.ForeignKey(Activity, blank=True,
        null=True, on_delete=models.SET_NULL)
    comment = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey('users.MyUser', blank=True,
        null=True, on_delete=models.SET_NULL) 
    