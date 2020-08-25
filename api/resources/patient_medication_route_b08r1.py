from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import PatientMedicationRouteB08R1


class PatientMedicationRouteB08R1Serializer(serializers.ModelSerializer):

    class Meta:
        model = PatientMedicationRouteB08R1
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientMedicationRouteB08R1DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientMedicationRouteB08R1
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class PatientMedicationRouteB08R1ViewSet(viewsets.ModelViewSet):
    queryset = PatientMedicationRouteB08R1.objects.all()
    serializer_class = PatientMedicationRouteB08R1Serializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class PatientMedicationRouteB08R1DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status """

    serializer_class = PatientMedicationRouteB08R1DeleteSerializer
    queryset = PatientMedicationRouteB08R1.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()