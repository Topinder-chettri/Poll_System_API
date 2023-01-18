from rest_framework import serializers
from .models import *

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['question']



class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['question','option']
