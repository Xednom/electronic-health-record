from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import PatientAddressB01, PatientContactB00


class PatientAddressB01Serializer(serializers.ModelSerializer):
    patient_contact = serializers.SlugRelatedField(slug_field="last_name",queryset=PatientContactB00.objects.all(), allow_null=True)

    class Meta:
        model = PatientAddressB01
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientAddressB01DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientAddressB01
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class PatientAddressB01ViewSet(viewsets.ModelViewSet):
    queryset = PatientAddressB01.objects.all()
    serializer_class = PatientAddressB01Serializer
    permission_classes = []
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class PatientAddressB01DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status only """

    serializer_class = PatientAddressB01DeleteSerializer
    queryset = PatientAddressB01.objects.all()
    lookup_field = 'id'
    permission_classes = []

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()