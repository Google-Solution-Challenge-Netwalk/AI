from django.urls import path
from .views import GarbageDecisionAPI
from . import views

urlpatterns = [
    path('', GarbageDecisionAPI.as_view()),
]