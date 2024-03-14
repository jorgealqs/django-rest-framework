from django.urls import path
from core.user.viewsets.test import testViewSet
from core.user.viewsets.userviewset import UserViewSetApiView
from rest_framework import routers
from core.auth.viewsets.register import CreateUserViewSet
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets.refresh import RefreshViewSet
from core.post.views import PostViewSet


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
  path("user/<str:public_id>", UserViewSetApiView.as_view()),
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
  path("post/<str:pk>/delete/", PostViewSet.as_view()),

  *router.urls,
]
