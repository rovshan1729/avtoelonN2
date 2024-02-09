from django.urls import path
from avto import views

urlpatterns = [
    path('post/', views.PostListAPIView.as_view()),
    path('contact/', views.ContactInfoAPIView.as_view()),
    path('save/note/', views.SaveAndNoteAPIView.as_view()),
    path('rent/own/', views.RentToOwnAPIView.as_view()),
    ]
