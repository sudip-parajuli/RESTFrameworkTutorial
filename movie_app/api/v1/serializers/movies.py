from rest_framework import serializers
from movie_app.models import Movie


##using Serializer
# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(max_length=50)
#     description=serializers.CharField(max_length=200)
#     active=serializers.BooleanField(default=True)
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         return instance

"""................................................................................................"""

# using ModelSerializer
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=['id', 'name', 'description', 'active']
