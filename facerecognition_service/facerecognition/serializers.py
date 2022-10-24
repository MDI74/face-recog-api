from rest_framework import serializers
from .models import *


#Класс сериализатор для преобразования полей в формат json для организаций
class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'


#Класс сериализатор для преобразования полей в формат json для сотрудников
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


#Класс сериализатор для преобразования полей в формат json для сессий
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
