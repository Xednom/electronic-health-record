from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import OrganizationStaffM03


class OrganizationStaffM03Serializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationStaffM03
        fields = "__all__"
        read_only_fields = ["date_modified"]


class OrganizationStaffM03DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationStaffM03
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class OrganizationStaffM03ViewSet(viewsets.ModelViewSet):
    queryset = OrganizationStaffM03.objects.all()
    serializer_class = OrganizationStaffM03Serializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class OrganizationStaffM03DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status """

    serializer_class = OrganizationStaffM03DeleteSerializer
    queryset = OrganizationStaffM03.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()