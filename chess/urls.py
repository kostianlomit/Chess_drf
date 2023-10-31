"""chess URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from chess_friends.views import ChessAPIList, ChessAPIDestroy, ChessAPIUpdate
from chess_friends.views import ChessViewSet
from rest_framework import routers



router = routers.DefaultRouter()  # при использовании class ChessViewSet(viewsets.ModelViewSet
router.register(r'chess', ChessViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))     # при DefaultRouter/SimpleRouter

    # path('api/v1/chesslist', ChessAPIList.as_view()), # permissions = IsAuthenticatedOrReadOnly
    # path('api/v1/chess/<int:pk>/', ChessAPIUpdate.as_view()),  # permissions = IsOwnerOrReadOnly
    # path('api/v1/chessdelete/<int:pk>/', ChessAPIDestroy.as_view()) # permissions = IsAdminOrReadOnly

]
