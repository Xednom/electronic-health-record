from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import OrganizationLocationM01


class OrganizationLocationM01Serializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationLocationM01
        fields = "__all__"
        read_only_fields = ["date_modified"]


class OrganizationLocationM01DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationLocationM01
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class OrganizationLocationM01ViewSet(viewsets.ModelViewSet):
    queryset = OrganizationLocationM01.objects.all()
    serializer_class = OrganizationLocationM01Serializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class OrganizationLocationM01DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status """

    serializer_class = OrganizationLocationM01DeleteSerializer
    queryset = OrganizationLocationM01.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()