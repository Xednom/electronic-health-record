from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import PatientContactB00


class PatientContactB00Serializer(serializers.ModelSerializer):

    class Meta:
        model = PatientContactB00
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientContactB00DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientContactB00
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class PatientContactB00ViewSet(viewsets.ModelViewSet):
    queryset = PatientContactB00.objects.all()
    serializer_class = PatientContactB00Serializer
    permission_classes = []
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class PatientContactB00DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status only """

    serializer_class = PatientContactB00DeleteSerializer
    queryset = PatientContactB00.objects.all()
    lookup_field = 'id'
    permission_classes = []

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()