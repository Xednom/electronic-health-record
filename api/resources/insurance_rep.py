from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import InsuranceB01


class InsuranceB01Serializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceB01
        fields = "__all__"
        read_only_fields = ["date_modified"]


class InsuranceB01DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = InsuranceB01
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class InsuranceB01ViewSet(viewsets.ModelViewSet):
    queryset = InsuranceB01.objects.all()
    serializer_class = InsuranceB01Serializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class InsuranceB01DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status """

    serializer_class = InsuranceB01DeleteSerializer
    queryset = InsuranceB01.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()