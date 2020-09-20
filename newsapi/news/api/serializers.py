from rest_framework import serializers
from news.api.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_data = serializers.DateField()
    active = serializers.BooleanField()
    create_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)

    def create(self,validated_data):
        Article.objects.create(**validated_data)

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
        
