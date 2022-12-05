from .models import Singer,Song
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer','duration']

class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True,read_only=True) #it put song detail form song models 
    # song = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')  #It create link of the songs
    song = serializers.SlugRelatedField(many=True,read_only=True,slug_field='duration')  #It create link of the songs
    song = serializers.HyperlinkedIdentityField(view_name='song-detail')  #It create link of the songs

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']