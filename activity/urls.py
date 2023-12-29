from django.urls import path
from .views import CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView, ActivityListCreateAPIView, ActivityRetrieveUpdateDestroyAPIView

app_name = 'activity'

urlpatterns = [
    path(r'comments/',  CommentListCreateAPIView.as_view(), name='comments_list'),
    path('activity', ActivityListCreateAPIView.as_view(), name='activity_list')
]