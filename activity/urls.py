from django.urls import path
from .views import (
    ActivityGetPostAPIView,
    ActivityPutDeleteAPIView,

    CommentGetPostAPIView,
    CommentPutDeleteAPIView,

    StatusGetAPIView,
)

app_name = 'activity'

urlpatterns = [
    path('activity/', ActivityGetPostAPIView.as_view()),
    path('activity/<int:id>/', ActivityPutDeleteAPIView.as_view()),

    path('comment/', CommentGetPostAPIView.as_view()),
    path('comment/<int:pk>/', CommentPutDeleteAPIView.as_view()),

    path('status/', StatusGetAPIView.as_view())


]