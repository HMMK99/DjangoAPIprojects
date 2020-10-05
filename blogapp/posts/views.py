from rest_framework import generics#, permissions

# Create your views here.

from .models import Post 
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
 #   permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
 #   permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    