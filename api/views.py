from django.shortcuts import render
from .models import Student
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from django.http import HttpResponse

# Create your views here.

def student_detail(request):
    stu= Student.objects.get(id =  1) # sql query
    # print(stu)
    serializer = StudentSerializer(stu)  # CONVERT IT INTO PYTHON NATIVE
    # print(serializer)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data) # CONVERT INTO JSON DATA
    # print(json_data)
    return HttpResponse(json_data,content_type='application/json')