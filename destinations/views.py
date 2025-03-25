# from rest_framework import viewsets
# from .models import Destination
# from .serializers import DestinationSerializer  # ✅ Make sure this is now correct

# class DestinationViewSet(viewsets.ModelViewSet):
#     queryset = Destination.objects.all()
#     serializer_class = DestinationSerializer


from rest_framework import generics
from .models import Destination
from .serializers import DestinationSerializer

class DestinationListView(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
