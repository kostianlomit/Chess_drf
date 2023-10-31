from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Chess


# пример класса сериализатора
# class ChessModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

class ChessSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()
    # photo =

    def create(self, validated_data):
        return Chess.objects.create(**validated_data)




# функция кодирования в json, на основе class ChessModel
# def encode():
#     model = ChessModel('Ferz', 'Content: Ferz')
#     model_sr = ChessSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)