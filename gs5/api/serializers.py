from rest_framework import serializers
from .models import Student

# validators
def starts_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError('Name should start be with r')

class StudentSerializer(serializers.ModelSerializer):
   # name = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100 , validators=[starts_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
       
  #field level validation
    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError('Seat Full')
        return value 

    #Object level Validation
    def validate(slf ,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower()!='ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data
