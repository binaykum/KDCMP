from django.shortcuts import render

from complaints.models import Villagename,Complaints
from rest_framework import viewsets
from rest_framework import permissions
from api_kdcmp.serialisers import VillageNameSerializer, ComplaintsSerializer


class complaintsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Complaints.objects.all() # .order_by('-date_joined')
    serializer_class = ComplaintsSerializer
    permission_classes = [permissions.IsAuthenticated]


class villagenameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Villagename.objects.all()
    serializer_class = VillageNameSerializer
    permission_classes = [permissions.IsAuthenticated]