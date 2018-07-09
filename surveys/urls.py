from django.urls import path

from . import views

urlpatterns = [
    path('responses/<int:question_id>', views.survey_responses, name="single_question"),
    path('responses/', views.survey_responses, name="response_list"),
    path('new/', views.new_question, name="new_question"),
    path('', views.index, name='index'),
]
