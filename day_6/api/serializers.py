from rest_framework import serializers
from .models import Category, Cast, Movie, Series

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    # Overriding the representation for GET requests (Retrieval)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Replace category IDs with their __str__ representations
        representation['categories'] = [str(cat) for cat in instance.categories.all()]
        
        # Replace cast IDs with their __str__ representations
        representation['casts'] = [str(cast) for cast in instance.casts.all()]
        
        return representation


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'