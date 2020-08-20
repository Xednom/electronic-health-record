from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import PatientPhone


class PatientPhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientPhone
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientPhoneViewSet(viewsets.ModelViewSet):
    queryset = PatientPhone.objects.all()
    serializer_class = PatientPhoneSerializer
    permission_classes = [IsAuthenticated]
