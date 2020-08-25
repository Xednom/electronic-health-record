from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import PatientMedicationB08


class PatientMedicationB08Serializer(serializers.ModelSerializer):

    class Meta:
        model = PatientMedicationB08
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientMedicationB08DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientMedicationB08
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class PatientMedicationB08ViewSet(viewsets.ModelViewSet):
    queryset = PatientMedicationB08.objects.all()
    serializer_class = PatientMedicationB08Serializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class PatientMedicationB08DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status """

    serializer_class = PatientMedicationB08DeleteSerializer
    queryset = PatientMedicationB08.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()