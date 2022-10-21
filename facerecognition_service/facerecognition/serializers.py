from rest_framework import serializers
from .models import *


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
