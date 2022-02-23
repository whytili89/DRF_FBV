from django.urls import path
from fbvApp import views

urlpatterns = [
    path('students/',views.student_list),
]