from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import InsuranceB00


class InsuranceB00Serializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceB00
        fields = "__all__"
        read_only_fields = ["date_modified"]


class InsuranceB00DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceB00
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class InsuranceB00ViewSet(viewsets.ModelViewSet):
    queryset = InsuranceB00.objects.all()
    serializer_class = InsuranceB00Serializer
    permission_classes = []
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class InsuranceB00DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status """

    serializer_class = InsuranceB00DeleteSerializer
    queryset = InsuranceB00.objects.all()
    lookup_field = 'id'
    permission_classes = []

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()