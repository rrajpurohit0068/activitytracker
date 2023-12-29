from rest_framework import generics, status, mixins
from rest_framework.views import APIView
from .models import Comment, Activity, Status
from .serializers import CommentSerializer, ActivitySerializer, StatusSerializer
from rest_framework.response import Response
from users.models import MyUser
from rest_framework.permissions import IsAuthenticated


class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comment.objects.all().filter(user_id__id=self.request.session.get("user").id)


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer

class ActivityListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    serializer_class = ActivitySerializer
    def get(self, request):
        print('IN Activit')
        serializer = self.serializer_class(Activity.objects.all().filter(user_id=request.user), many=True)
        print('get LLLL')
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ActivityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer
    


