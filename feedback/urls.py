from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('done', views.DoneView.as_view()),
    path('', views.FeedBackView.as_view(), name='index'),
    path('<int:id_feedback>', views.FeedBackUpdateView.as_view(), name='feedback-update'),
    path('list', views.ListFeedBack.as_view(), name='list-feedbacks'),
    path('detail/<id_feedback>', views.DetailFeedBack.as_view(), name='detail-feedback'),
]