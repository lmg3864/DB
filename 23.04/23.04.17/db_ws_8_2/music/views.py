from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Music
from .serializers import MusicListSerializer, MusicSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        musics = Music.objects.all()
        serializer = MusicListSerializer(musics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

@api_view(['GET'])
def music_detail(request, music_pk):
    music = Music.objects.get(pk=music_pk)
    serializer = MusicSerializer(music)
    return Response(serializer.data)