from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import PatientFamilyB05S


class PatientFamilyB05SSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientFamilyB05S
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientFamilyB05SDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientFamilyB05S
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class PatientFamilyB05SViewSet(viewsets.ModelViewSet):
    queryset = PatientFamilyB05S.objects.all()
    serializer_class = PatientFamilyB05SSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class PatientFamilyB05SDeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status only """

    serializer_class = PatientFamilyB05SDeleteSerializer
    queryset = PatientFamilyB05S.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()