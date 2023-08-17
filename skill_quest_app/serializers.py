from rest_framework import serializers

from .models import Course, CourseQuiz, CourseQuizResult, Profile, InterestQuiz, CourseEnrollment


class CourseSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    creator = serializers.CharField(max_length=200)
    description = serializers.CharField()
    source_link = serializers.CharField()

    def create(self, validated_data):
        return Course.objects.create(
            title=validated_data.get("title"),
            creator=validated_data.get("creator"),
            description=validated_data.get("description"),
            source_link=validated_data.get("source_link"),
        )

    class Meta:
        model = Course
        fields = (
            'title',
            'creator',
            'source_link',
            'description',
            'id'
        )


class CourseQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseQuiz
        fields = '__all__'


class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseQuizResult
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField(max_length=500)
    location = serializers.CharField(max_length=200)
    short_intro = serializers.CharField(max_length=200)
    profile_image = serializers.ImageField()

    def create(self, validated_data):
        return Profile.objects.create(
            name=f"{validated_data.get('first_name')} {validated_data.get('last_name')}",
            email=validated_data.get("email"),
            short_intro=validated_data.get("short_intro"),
            profile_image=validated_data.get("profile_image"),
            profession=validated_data.get("profession")
        )

    class Meta:
        model = Profile
    fields = (
        'user_id',
        'first_name',
        'last_name',
        'email'
        'location',
        'short_intro',
        'profile_image'
    )


class InterestQuizSerializer(serializers.ModelSerializer):
    question = serializers.CharField(max_length=200)
    option_1 = serializers.CharField(max_length=200)
    option_2 = serializers.CharField(max_length=200)
    option_3 = serializers.CharField(max_length=200)
    option_4 = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return InterestQuiz.objects.create(
            question=validated_data.get('question'),
            option_1=validated_data.get("option_1"),
            option_2=validated_data.get("option_2"),
            option_3=validated_data.get("option_3"),
            option_4=validated_data.get("option_4")
        )

    class Meta:
        model = InterestQuiz
        fields = (
            'question',
            'option_1',
            'option_2',
            'option_3',
            'option_4'
        )


class CourseQuizResultSerializer(serializers.ModelSerializer):
    quiz = CourseQuizSerializer()

    class Meta:
        model = CourseQuizResult
        fields = ['user', 'quiz', 'answers']

    def create(self, validated_data):
        quiz_data = validated_data.pop('quiz')  # Extract quiz data from nested serializer
        quiz = CourseQuiz.objects.create(**quiz_data)

        course_quiz_result = CourseQuizResult.objects.create(quiz=quiz, **validated_data)
        return course_quiz_result


class CourseEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = '__all__'
