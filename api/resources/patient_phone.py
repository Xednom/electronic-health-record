from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import PatientPhoneB02


class PatientPhoneB02Serializer(serializers.ModelSerializer):

    class Meta:
        model = PatientPhoneB02
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientPhoneB02ViewSet(viewsets.ModelViewSet):
    queryset = PatientPhoneB02.objects.all()
    serializer_class = PatientPhoneB02Serializer
    permission_classes = [IsAuthenticated]
