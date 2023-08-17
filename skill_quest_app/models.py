from django.contrib.auth.models import User
from django.db import models


class CourseQuiz(models.Model):
    question = models.CharField(max_length=200)
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    answer = models.IntegerField(choices=[(1, "Option 1"), (2, "Option 2"), (3, "Option 3"), (4, "Option 4")])

    def __str__(self):
        return str(self.question)


class Course(models.Model):
    title = models.CharField(max_length=200)
    creator = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    source_link = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CourseEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, default="default.png")
    created = models.DateTimeField(auto_now_add=True)
    enrolled_courses = models.ManyToManyField(Course)
    profession = models.CharField(max_length=50)


class CourseQuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(CourseQuiz, on_delete=models.CASCADE)
    answers = models.JSONField()
    quiz_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class InterestQuiz(models.Model):
    question = models.CharField(max_length=200)
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.question}"


class InterestQuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(InterestQuiz, on_delete=models.CASCADE)
    answers = models.JSONField()
    quiz_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
