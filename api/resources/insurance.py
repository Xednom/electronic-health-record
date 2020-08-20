from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import Insurance


class InsuranceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Insurance
        fields = "__all__"
        read_only_fields = ["date_modified"]


class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [IsAuthenticated]
