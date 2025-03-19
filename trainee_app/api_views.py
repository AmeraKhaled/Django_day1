from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Trainee, Course
from .serializers import TraineeSerializer, TrackSerializer


class TraineeListCreateAPI(generics.ListCreateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

class TraineeUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer


@api_view(['PUT'])
def update_track(request, pk):
    try:
        track = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({"error": "Track not found"}, status=404)

    serializer = TrackSerializer(track, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=400)


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = TrackSerializer
