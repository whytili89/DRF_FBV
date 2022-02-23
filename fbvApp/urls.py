from django.urls import path
from fbvApp import views

urlpatterns = [
    path('students/',views.student_list),
    path('student/<int:pk>', views.student_detail),
]