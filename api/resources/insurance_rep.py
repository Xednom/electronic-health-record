from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import InsuranceB01


class InsuranceB01Serializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceB01
        fields = "__all__"
        read_only_fields = ["date_modified"]


class InsuranceB01ViewSet(viewsets.ModelViewSet):
    queryset = InsuranceB01.objects.all()
    serializer_class = InsuranceB01Serializer
    permission_classes = [IsAuthenticated]
