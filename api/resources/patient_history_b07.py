from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import PatientHistoryB07


class PatientHistoryB07Serializer(serializers.ModelSerializer):

    class Meta:
        model = PatientHistoryB07
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientHistoryB07DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientHistoryB07
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class PatientHistoryB07ViewSet(viewsets.ModelViewSet):
    queryset = PatientHistoryB07.objects.all()
    serializer_class = PatientHistoryB07Serializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class PatientHistoryB07DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status only """

    serializer_class = PatientHistoryB07DeleteSerializer
    queryset = PatientHistoryB07.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()