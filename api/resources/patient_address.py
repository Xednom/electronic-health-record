from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import PatientAddress


class PatientAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientAddress
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientAddressViewSet(viewsets.ModelViewSet):
    queryset = PatientAddress.objects.all()
    serializer_class = PatientAddressSerializer
    permission_classes = [IsAuthenticated]
