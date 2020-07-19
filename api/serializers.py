from rest_framework import serializers

from .models import Post, Comment, Follow, User, Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        # fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        # fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

# class FollowSerializer(serializers.ModelSerializer):
#
#     #user = serializers.SlugRelatedField(read_only=True, slug_field='username')#, default=CurrentUserDefault())
#     #following = serializers.SlugRelatedField(read_only=False, slug_field='username', queryset=User.objects.all())
#     following = serializers.ReadOnlyField(read_only=False,
#                                              slug_field='username',
#                                              queryset=User.objects.all())
#
#     class Meta:
#         model = Follow
#         fields = ['user', 'following']
#         # validators = [UniqueTogetherValidator(queryset=Follow.objects.all(), fields=['user', 'following'])]
