from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import CompanyB00


class CompanyB00Serializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyB00
        fields = "__all__"
        read_only_fields = ["date_modified"]


class CompanyB00ViewSet(viewsets.ModelViewSet):
    queryset = CompanyB00.objects.all()
    serializer_class = CompanyB00Serializer
    permission_classes = [IsAuthenticated]
