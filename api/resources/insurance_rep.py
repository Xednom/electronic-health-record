from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import InsuranceRepresentative


class InsuranceRepresentativeSerializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceRepresentative
        fields = "__all__"
        read_only_fields = ["date_modified"]


class InsuranceRepresentativeViewSet(viewsets.ModelViewSet):
    queryset = InsuranceRepresentative.objects.all()
    serializer_class = InsuranceRepresentativeSerializer
    permission_classes = [IsAuthenticated]
