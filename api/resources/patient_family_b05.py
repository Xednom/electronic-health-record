from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import PatientFamilyB05


class PatientFamilyB05Serializer(serializers.ModelSerializer):

    class Meta:
        model = PatientFamilyB05
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientFamilyB05DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientFamilyB05
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class PatientFamilyB05ViewSet(viewsets.ModelViewSet):
    queryset = PatientFamilyB05.objects.all()
    serializer_class = PatientFamilyB05Serializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class PatientFamilyB05DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status only """

    serializer_class = PatientFamilyB05DeleteSerializer
    queryset = PatientFamilyB05.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()