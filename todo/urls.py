from django.urls import URLPattern, path

from .views import DoneTodosAPIView, TodosAPIView, TodoAPIView, DoneTodoAPIView

urlpatterns = [
  path('todo/', TodosAPIView.as_view()),
  path('todo/<int:pk>/', TodoAPIView.as_view()),
  path('done/', DoneTodosAPIView.as_view()),
  path('done/<int:pk>/', DoneTodoAPIView.as_view()),
]