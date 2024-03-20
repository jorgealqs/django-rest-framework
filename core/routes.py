from django.urls import path
from core.user.viewsets.test import testViewSet
from core.user.viewsets.userviewset import UserViewSetApiView
from rest_framework import routers
from core.auth.viewsets.register import CreateUserViewSet
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets.refresh import RefreshViewSet
from core.post.views import PostViewSet
from core.post.viewsets.likeuser import LikeUser
from core.post.viewsets.removelikeuser import RemoveLikeUser
from core.comment.viewsets.list import CommentViewSet
from core.comment.viewsets.get_a_comment_by_post import CommentDetailView



router = routers.SimpleRouter()

# ############################################################
######### #
# ################### USER ###################### #
# ############################################################
######### #
# router.register(r'login', LoginViewSet, basename='user')

urlpatterns = [
  path("test/", testViewSet.as_view()),
  # ############################################################
  ######### #
  # ################### USER ###################### #
  # ############################################################
  ######### #
  path("user/", UserViewSetApiView.as_view()),
  path("user/<str:public_id>/", UserViewSetApiView.as_view()),
  path("user/create/", CreateUserViewSet.as_view()),
  # ############################################################
  ######### #
  # ################### AUTH ###################### #
  # ############################################################
  ######### #
  path("login/", LoginViewSet.as_view()),
  path("refresh/token/", RefreshViewSet.as_view()),
  # ############################################################
  ######### #
  # ################### Post ###################### #
  # ############################################################
  ######### #
  path("post/", PostViewSet.as_view()),
  path("post/<str:pk>/", PostViewSet.as_view()),
  path("post/author/<str:author_public_id>/", PostViewSet.as_view()),
  path("post/<str:pk>/update/", PostViewSet.as_view()),
  path("post/<str:pk>/delete/", PostViewSet.as_view()),
  path("post/<str:pk>/like/", LikeUser.as_view()),
  path("post/<str:pk>/remove_like/", RemoveLikeUser.as_view()),
  # ############################################################
  ######### #
  # ################### Comment ###################### #
  # ############################################################
  ######### #
  path("post/<str:pk_post>/comment/", CommentViewSet.as_view()),
  path("post/<str:pk_post>/comment/<str:pk_comment>/", CommentDetailView.as_view())

  # *router.urls,
]
