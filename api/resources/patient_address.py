from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import PatientAddressB01


class PatientAddressB01Serializer(serializers.ModelSerializer):

    class Meta:
        model = PatientAddressB01
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientAddressB01ViewSet(viewsets.ModelViewSet):
    queryset = PatientAddressB01.objects.all()
    serializer_class = PatientAddressB01Serializer
    permission_classes = [IsAuthenticated]
