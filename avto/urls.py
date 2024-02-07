from django.urls import path, include
from avto import views

urlpatterns = [path("", views.PostListAPIView.as_view())]
