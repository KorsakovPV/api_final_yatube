# TODO:  Напишите свой вариант
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api import serializers
from api.models import Post, Group, Follow
from api.permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Post.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('group', )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user)

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Group.objects.all()

class FollowViewSet(viewsets.ModelViewSet):
    pass