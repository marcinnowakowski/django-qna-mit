from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='question_list'),
    path('create/', views.QuestionCreateView.as_view(), name='question_create'),  # Ensure this is present
    path('<slug:slug>/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('<slug:slug>/edit/', views.QuestionEditView.as_view(), name='question_edit'),
]