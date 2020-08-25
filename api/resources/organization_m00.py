from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import OrganizationM00


class OrganizationM00Serializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationM00
        fields = "__all__"
        read_only_fields = ["date_modified"]


class OrganizationM00DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationM00
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class OrganizationM00ViewSet(viewsets.ModelViewSet):
    queryset = OrganizationM00.objects.all()
    serializer_class = OrganizationM00Serializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class OrganizationM00DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status """

    serializer_class = OrganizationM00DeleteSerializer
    queryset = OrganizationM00.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()