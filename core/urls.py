from django.urls import path

from . import views

urlpatterns = [
    path('', views.voting_view, name='voting'),
    path('success', views.success_view, name='success'),
]
