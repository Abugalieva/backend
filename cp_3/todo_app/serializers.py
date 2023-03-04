from rest_framework import serializers
from todo_app.models import TodoList, Todo

class TodolistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(min_length=5, max_length=100, allow_null=False)

    def create(self, validated_data):
        todolist = TodoList(**validated_data)
        todolist.save()
        return todolist

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(min_length=5, max_length=200, allow_null=False)
    done = serializers.BooleanField(default=False, allow_null=False)
    todolist = TodolistSerializer(required=False, read_only=True)
    todolist_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        todo = Todo(**validated_data)
        todo.save()
        return todo

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.todolist_id = validated_data.get('todolist_id', instance.todolist_id)

        instance.save()
        return instance