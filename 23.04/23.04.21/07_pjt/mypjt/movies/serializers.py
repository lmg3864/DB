from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name')

class ActorSerializer(serializers.ModelSerializer):
    class MovieToActor(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movies = MovieToActor(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ('id', 'movies', 'name')

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview')

class MovieSerializer(serializers.ModelSerializer):
    class ActorToMovie(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)
    actors = ActorToMovie(many=True, read_only=True)
    class ReviewToMovie(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content')
    review_set = ReviewToMovie(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('id', 'actors', 'review_set', 'title', 'overview', 'release_date', 'poster_path')

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content')

class ReviewSerializer(serializers.ModelSerializer):
    class MovieToReview(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movie = MovieToReview(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'content')