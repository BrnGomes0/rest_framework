from app.models import Todo

from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields= ['id', 'name', 'done', 'created_at'] # Campos que vai ser transformando em JSON