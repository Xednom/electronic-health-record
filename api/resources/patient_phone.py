from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import PatientPhoneB02, PatientContactB00


class PatientPhoneB02Serializer(serializers.ModelSerializer):
    patient_contact = serializers.SlugRelatedField(slug_field="last_name",queryset=PatientContactB00.objects.all(), allow_null=True)

    class Meta:
        model = PatientPhoneB02
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientPhoneB02DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientPhoneB02
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class PatientPhoneB02ViewSet(viewsets.ModelViewSet):
    queryset = PatientPhoneB02.objects.all()
    serializer_class = PatientPhoneB02Serializer
    permission_classes = []
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class PatientPhoneB02DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status only """

    serializer_class = PatientPhoneB02DeleteSerializer
    queryset = PatientPhoneB02.objects.all()
    lookup_field = 'id'
    permission_classes = []

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()