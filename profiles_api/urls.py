from django.urls import path
from profiles_api import views

urlpatterns = [
    path('nabiya/', views.HelloApiView.as_view()),
]
