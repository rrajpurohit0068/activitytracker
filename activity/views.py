from rest_framework import generics, status, mixins
from rest_framework.views import APIView
from .models import Comment, Activity, Status
from .serializers import CommentSerializer, ActivitySerializer, StatusSerializer
from rest_framework.response import Response
from users.models import MyUser
from rest_framework.permissions import IsAuthenticated

# activity apis
class ActivityGetPostAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    


    def list(self, request):
        print('start')
        print(request, request.user, Activity.objects.filter(user_id=request.user))
        serializer = ActivitySerializer(Activity.objects.filter(user_id=request.user), many=True)
        print('done')
        return Response(serializer.data)
    

    
    
class ActivityPutDeleteAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    lookup_field = 'id'
    

# comment api

class CommentGetPostAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CommentSerializer()
    def get(self, request, activity_id):
        serializer = CommentSerializer(Comment.objects.all().filter(activity_id=activity_id))
        return Response(serializer.data)

class CommentPutDeleteAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CommentSerializer
    queryset = Activity.objects.all()
    lookup_field = 'id'



# status api

class StatusGetAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

