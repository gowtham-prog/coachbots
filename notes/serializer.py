from rest_framework import serializers
from .models import *
from rest_framework.serializers import Serializer,FileField

class NoteSerializer(serializers.ModelSerializer):
    class Meta :
        model = Note
        fields = '__all__'
    
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'