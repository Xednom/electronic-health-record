from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import InsuranceB00


class InsuranceB00Serializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceB00
        fields = "__all__"
        read_only_fields = ["date_modified"]


class InsuranceB00ViewSet(viewsets.ModelViewSet):
    queryset = InsuranceB00.objects.all()
    serializer_class = InsuranceB00Serializer
    permission_classes = [IsAuthenticated]
