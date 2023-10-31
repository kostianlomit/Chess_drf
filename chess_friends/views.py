from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

from .models import Chess, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serialazers import ChessSerializer


# Выполнение CRUD запросов
class ChessViewSet(viewsets.ModelViewSet):
    queryset = Chess.objects.all()
    serializer_class = ChessSerializer
    permission_classes = (IsAdminOrReadOnly,)

    # спомощью декоратора создаем новый маршрут для вывода категорий http://127.0.0.1:8000/api/v1/chess/category/
    @action(methods=['get'], detail=True) # False если хотим вывести все названия
    def category(selfself, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})



# # для ограничения доступа используем permissions_classes
# # смотреть могут только user  admin
# class ChessAPIList(generics.ListCreateAPIView):
#     queryset = Chess.objects.all()
#     serializer_class = ChessSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#
# # создавать могут только admin
# class ChessAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Chess.objects.all()
#     serializer_class = ChessSerializer
#     permission_classes = (IsOwnerOrReadOnly,)
#
# # удалять могут только admin
# class ChessAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Chess.objects.all()
#     serializer_class = ChessSerializer
#     permission_classes = (IsAdminOrReadOnly,)


from chess_friends.forms import FeedbackForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

class FeedbackFormView(FormView):
    template_name = "feedback/feedback.html"
    form_class = FeedbackForm
    success_url = "/success/"

    def form_valid(self, form):
        form.send_email()
