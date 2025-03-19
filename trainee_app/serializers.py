from rest_framework import serializers
from .models import Trainee, Course

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
