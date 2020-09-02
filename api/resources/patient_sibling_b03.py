from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import PatientSiblingB03, PatientContactB00


class PatientSiblingB03Serializer(serializers.ModelSerializer):
    patient_contact_b00_rec = serializers.SlugRelatedField(slug_field="last_name",queryset=PatientContactB00.objects.all(), allow_null=True)

    class Meta:
        model = PatientSiblingB03
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientSiblingB03DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientSiblingB03
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class PatientSiblingB03ViewSet(viewsets.ModelViewSet):
    queryset = PatientSiblingB03.objects.all()
    serializer_class = PatientSiblingB03Serializer
    permission_classes = []
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class PatientSiblingB03DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status only """

    serializer_class = PatientSiblingB03DeleteSerializer
    queryset = PatientSiblingB03.objects.all()
    lookup_field = 'id'
    permission_classes = []

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()