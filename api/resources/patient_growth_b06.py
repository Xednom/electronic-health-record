from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import PatientGrowthB06


class PatientGrowthB06Serializer(serializers.ModelSerializer):

    class Meta:
        model = PatientGrowthB06
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientGrowthB06DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientGrowthB06
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class PatientGrowthB06ViewSet(viewsets.ModelViewSet):
    queryset = PatientGrowthB06.objects.all()
    serializer_class = PatientGrowthB06Serializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class PatientGrowthB06DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status only """

    serializer_class = PatientGrowthB06DeleteSerializer
    queryset = PatientGrowthB06.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()