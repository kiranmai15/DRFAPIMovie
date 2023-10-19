from rest_framework import serializers
#import models
from watchlist_app.models import WatchList, StreamPlatform, Review
#To accept tags through a REST API call we need to add the following to our Serializer:
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)

# Using Model Serilizer 
class ReviewSerializer(serializers.ModelSerializer):
      review_user = serializers.StringRelatedField(read_only=True)
     
      class Meta:
        model = Review
        fields = "__all__"
        
class WatchListSerializer(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField()
    image = serializers.ImageField(max_length=None,use_url=True)
    # 1 watchlist can have many reviews
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = WatchList
        fields = ('id', 'title','storyline', 'streamingPlatform','active','tags','image','reviews')
        # fields = ['id', 'name','title', 'desc']
        # exclude = ['active']        
        
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    #Using Nested Serializer one to many
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        

# # Using Normal Serializer
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     desc = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#        return Movie.objects.create(**validated_data)
   
#    #instance carries old data & validated_data carries new data
#     def update(self, instance, validated_data):
#         # Map the old data to the new data
#         instance.name = validated_data.get('name', instance.name)
#         instance.desc = validated_data.get('desc', instance.desc)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    # def validate(self, data):
    #     if data['name'] == data['desc']:
    #         raise serializers.ValidationError("Title and Description should be different")
    #     else:
    #       return data
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError({'name' : 'Name must be at least 2 characters'})
    #     else:
    #         return value