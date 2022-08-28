from django.urls import path
from . import views

urlpatterns = [
    path('nodes/', views.display_nodes),
    path('pods/', views.display_pods)
]