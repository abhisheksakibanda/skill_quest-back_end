from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from skill_quest_app.models import Course, CourseQuizResult, CourseQuiz, InterestQuiz, CourseEnrollment
from skill_quest_app.serializers import CourseSerializer, QuizResultSerializer, CourseQuizSerializer, ProfileSerializer, \
    InterestQuizSerializer, CourseQuizResultSerializer, CourseEnrollmentSerializer


# Create your views here.
class ListCoursesView(APIView):
    def get(self, request, id=None):
        queryset = Course.objects.filter(id=id) if id else Course.objects.all()
        read_serializer = CourseSerializer(queryset, many=True, allow_empty=True)
        return Response(read_serializer.data)


class PostCoursesView(APIView):
    def post(self, request):
        create_serializer = CourseSerializer(data=request.data)
        if create_serializer.is_valid():
            course_object = create_serializer.save()
            read_serializer = CourseSerializer(course_object)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        return Response(create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_course(request, pk):
    data = request.data
    course = Course.objects.get(id=pk)
    serializer = CourseSerializer(course, data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_course(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return Response("The course has been deleted...")


@api_view(['GET'])
def get_quiz_results():
    quiz_result = CourseQuizResult.objects.all()
    read_serializer = QuizResultSerializer(quiz_result)
    return Response(read_serializer.data)


@api_view(['GET'])
def get_course_quiz(request, course_id):
    queryset = CourseQuiz.objects.filter(id=course_id) if id else CourseQuiz.objects.all()
    serializer = CourseQuizSerializer(queryset, many=True)
    return Response(serializer.data)


class ProfileView(APIView):
    def get(self, request, id=None):
        queryset = Course.objects.filter(id=id) if id else Course.objects.all()
        read_serializer = ProfileSerializer(queryset)
        return Response(read_serializer.data)

    def post(self, request):
        create_serializer = ProfileSerializer(data=request.data)
        if create_serializer.is_valid():
            course_object = create_serializer.save()
            read_serializer = CourseSerializer(course_object)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        return Response(create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_interest_quiz(request, id):
    queryset = InterestQuiz.objects.filter(id=id) if id else CourseQuiz.objects.all()
    serializer = InterestQuizSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_interest_quiz(request):
    create_serializer = InterestQuizSerializer(data=request.data)
    if create_serializer.is_valid():
        course_object = create_serializer.save()
        read_serializer = CourseSerializer(course_object)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)
    return Response(create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseQuizResultCreateView(APIView):
    def post(self, request):
        serializer = CourseQuizResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_enrolled_course(request):
    courses = CourseEnrollment.objects.all()
    serializer = CourseEnrollmentSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_enrolled_course(request):
    data = request.data
    course = CourseEnrollment.objects.create(description=data['description'])
    serializer = CourseEnrollmentSerializer(course, many=False)
    return Response(serializer.data)
