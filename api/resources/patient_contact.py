from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import PatientContactB00


class PatientContactB00Serializer(serializers.ModelSerializer):

    class Meta:
        model = PatientContactB00
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientContactB00ViewSet(viewsets.ModelViewSet):
    queryset = PatientContactB00.objects.all()
    serializer_class = PatientContactB00Serializer
    permission_classes = [IsAuthenticated]
