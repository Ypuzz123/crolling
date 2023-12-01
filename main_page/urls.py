from django.urls import path
from . import views

urlpatterns = [
    path('', views.weblist_view, name='weblist'),
    path('save_word/', views.save_word, name='saveword'),
]