from django.urls import path
from . import views


urlpatterns = [
    path('question_post/', views.questionpost, name='question_post'),
    path('question_all/<int:pk>', views.questionall, name='Questionall'),
    path('choice_post/', views.questionpost, name='choice_post'),
    path('choice_all/<int:pk>', views.questionall, name='choiceall'),


]