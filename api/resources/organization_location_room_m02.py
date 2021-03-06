from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import OrganizationLocationRoomM02


class OrganizationLocationRoomM02Serializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationLocationRoomM02
        fields = "__all__"
        read_only_fields = ["date_modified"]


class OrganizationLocationRoomM02DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationLocationRoomM02
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class OrganizationLocationRoomM02ViewSet(viewsets.ModelViewSet):
    queryset = OrganizationLocationRoomM02.objects.all()
    serializer_class = OrganizationLocationRoomM02Serializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class OrganizationLocationRoomM02DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status """

    serializer_class = OrganizationLocationRoomM02DeleteSerializer
    queryset = OrganizationLocationRoomM02.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()