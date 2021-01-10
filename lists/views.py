from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import List

# Create your views here.

class ListSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = List
		fields = ['name', 'description', 'created_at', 'updated_at']

class ListViewSet(viewsets.ModelViewSet):
	queryset = List.objects.all()
	serializer_class = ListSerializer
