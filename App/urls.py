from django.urls import path
from .views import *
urlpatterns = [
    path('Subject/', SubjectListView.as_view()),
    path('Subject/<int:pk>/', SubjectRetrieveUpdateDestroyAPIView.as_view()),

    path('Student/', StudentListView.as_view()),
    path('Student/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view()),

    path('Class/', ClassListView.as_view()),
    path('Class/<int:pk>/', ClassRetrieveUpdateDestroyAPIView.as_view()),
]
