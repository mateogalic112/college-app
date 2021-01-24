from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    # Student
    path('students', student_list, name="students"),
    path('students/<int:student_id>', enroll_paper, name="enroll_paper"),
    # Subject
    path('subjects', subject_list, name="subjects"),
    #Enroll
    path('enrolled/remove/<int:enroll_id>', remove_enrolled_subject, name="remove_enrolled"),
    path('enrolled/add', add_enrolled_subject, name="add_enrolled"),
    path('enrolled/update/<int:enroll_id>', update_enrolled_subject, name="update_enrolled"),
]