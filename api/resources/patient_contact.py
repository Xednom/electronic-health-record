from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import PatientContact


class PatientContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientContact
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientContactViewSet(viewsets.ModelViewSet):
    queryset = PatientContact.objects.all()
    serializer_class = PatientContactSerializer
    permission_classes = [IsAuthenticated]
