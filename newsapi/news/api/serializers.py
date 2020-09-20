from datetime               import datetime
from django.utils.timesince import timesince
from rest_framework         import serializers
from news.api.models        import Article

class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = Article
        exclude = ("id",)

    def get_time_since_publication(self,object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date,now)
        return time_delta

    def create(self,validated_data):
        return Article.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.author = validated_data.get('author',instance.author)
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.body = validated_data.get('body',instance.body)
        instance.location = validated_data.get('location',instance.location)
        instance.publication_data = validated_data.get('publication_data',instance.publication_data)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance

    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and Description must be different from one another!")
        return data
    
    def validate_title(self,value): 
        if len(value) > 60:
            raise serializers.ValidationError("The title has to be at least 60 chars long!")
        return value 
