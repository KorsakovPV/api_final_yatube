from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, )

from api import views

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='Post')
router.register(r'posts/(?P<post_id>\d+)/comments', views.CommentViewSet, basename='Comment')
router.register('follow', views.FollowViewSet, basename='Follow')
router.register('group', views.GroupViewSet, basename='Group')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'), ]
