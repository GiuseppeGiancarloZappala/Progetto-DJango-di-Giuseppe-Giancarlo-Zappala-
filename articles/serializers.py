from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Article


class lasthourpostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class appearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ('description')
        fields = ['body']

