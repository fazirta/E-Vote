from django.urls import path

from . import views

urlpatterns = [
    path('', views.Vote_view, name='Vote'),
    path('success', views.success_view, name='success'),
    path('result', views.result_view, name='result'),
]
