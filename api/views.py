from django.shortcuts import render
from .models import Student
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from django.http import HttpResponse

# Create your views here.
# query set - single student
def student_detail(request, pk):
    stu= Student.objects.get(id =  pk) # sql query
    # print(stu)
    serializer = StudentSerializer(stu)  # CONVERT IT INTO PYTHON NATIVE
    # print(serializer)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data) # CONVERT INTO JSON DATA
    # print(json_data)
    return HttpResponse(json_data,content_type='application/json')

#Query set  - all student data
def student_list(request):
    stu= Student.objects.all() # sql query
    # print(stu)
    serializer = StudentSerializer(stu, many=True)  # CONVERT IT INTO PYTHON NATIVE
    # print(serializer)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data) # CONVERT INTO JSON DATA
    # print(json_data)
    return HttpResponse(json_data,content_type='application/json')