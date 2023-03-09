from django.urls import path
from . import views

urlpatterns = [
    path('employer-signup/', views.ListCreateEmployerView.as_view())

]
