from rest_framework import serializers
from movie_app.models import Movie,StreamPlatform,WatchList


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
    status=serializers.SerializerMethodField() #implemented custom serializer field
    class Meta:
        model=Movie
        # fields=['id', 'name', 'description', 'active']
        fields='__all__'

    def get_status(self, obj):
        if obj.active:
            return "Movie is running successfully!"
        return "Not Available!"



    #field level validations

    def validate_name(self,value):
        not_allowed_char = ['*', '#', '@', '+', '&', '%', '/', '{', '}', '[', ']']

        if len(value)<2:
            raise serializers.ValidationError("Movie name must contain at least 2 characters!")
        if any(char in value for char in not_allowed_char):
            raise serializers.ValidationError("Movie name must not contain any special characters")
        if not value[0].isupper():
            raise serializers.ValidationError("First letter of name must be uppercase")
        if Movie.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Movie with this name already exist.")
        return value

    def validate_detail(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Movie description must contain at least 10 characters!")
        return value

    def validate(self, attrs):
        banned_words=['bugger', 'bullshit', 'bastard', 'crap', 'dammit', 'damn',
                        'damned', 'damn it', 'god dammit', 'goddammit', 'God damn', 'god damn', 'goddamn',                                                                    'Goddamn', 'goddamned',
                        'goddamnit', 'godsdamn', 'hell', 'holy shit''horseshit',
                        'in shit', 'nigga', 'nigra', 'Jesus Christ', 'shit', ]

        if attrs['name'].lower().strip()==attrs['description'].lower().strip():
            raise serializers.ValidationError("name and description must not be same")

        for word in banned_words:
            if word in attrs['name'].lower().strip() or word in attrs['description'.lower().strip()]:
                raise serializers.ValidationError("Movie name or description contains improper words")
        return attrs


"""............................................................................................................"""



"""creating WatchList serializer and StreamPlatform serializer"""

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model=StreamPlatform
        fields='__all__'


class WatchListSerializer(serializers.ModelSerializer):
    status=serializers.SerializerMethodField() #implemented custom serializer field
    class Meta:
        model=WatchList
        fields='__all__'

    def get_status(self, obj):
        if obj.active:
            return "Running successfully!"
        return "Not Available!"


