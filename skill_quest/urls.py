"""
URL configuration for skill_quest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from skill_quest_app import views
from skill_quest_app.views import ListCoursesView, PostCoursesView, ProfileView, CourseQuizResultCreateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Courses APIs
    path('getCourses/', ListCoursesView.as_view()),
    path('getCourse/<int:id>/', ListCoursesView.as_view()),
    path('postCourse/', PostCoursesView.as_view()),
    path('updateCourse/<int:pk>/', views.update_course),
    path('deleteCourse/<int:pk>/', views.delete_course),

    # CourseQuiz APIs
    path('getCourseQuiz/<int:course_id>', views.get_course_quiz),

    path('getQuizResults/', views.get_quiz_results),

    # Profile APIs
    path('getProfile/<int:course_id>', ProfileView.as_view()),
    path('newProfile/', ProfileView.as_view()),

    # InterestQuiz APIs
    path('getInterestQuiz/<int:id>', views.get_interest_quiz),
    path('postInterestQuiz/', views.post_interest_quiz),

    # CourseQuizResults APIs
    path('postQuizResults/', CourseQuizResultCreateView.as_view()),

    # CoursesEnrollment APIs
    path('getEnrollCourse/', views.get_enrolled_course),
    path('postEnrollCourse/', views.create_enrolled_course)
]
