from django.contrib import admin

from .models import CourseQuiz, Course, CourseEnrollment, Profile, CourseQuizResult, InterestQuiz, InterestQuizResult

# Register your models here.
admin.site.register(CourseQuiz)
admin.site.register(Course)
admin.site.register(CourseEnrollment)
admin.site.register(Profile)
admin.site.register(CourseQuizResult)
admin.site.register(InterestQuiz)
admin.site.register(InterestQuizResult)
