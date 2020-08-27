from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import CompanyB00


class CompanyB00Serializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyB00
        fields = "__all__"
        read_only_fields = ["date_modified"]


class CompanyB00DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyB00
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class CompanyB00ViewSet(viewsets.ModelViewSet):
    queryset = CompanyB00.objects.all()
    serializer_class = CompanyB00Serializer
    permission_classes = []
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class CompanyB00DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status """

    serializer_class = CompanyB00DeleteSerializer
    queryset = CompanyB00.objects.all()
    lookup_field = 'id'
    permission_classes = []

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()