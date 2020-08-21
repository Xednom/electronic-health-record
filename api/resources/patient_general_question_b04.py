from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import PatientGeneralQuestionB04


class PatientGeneralQuestionB04Serializer(serializers.ModelSerializer):

    class Meta:
        model = PatientGeneralQuestionB04
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientGeneralQuestionB04DeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientGeneralQuestionB04
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class PatientGeneralQuestionB04ViewSet(viewsets.ModelViewSet):
    queryset = PatientGeneralQuestionB04.objects.all()
    serializer_class = PatientGeneralQuestionB04Serializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class PatientGeneralQuestionB04DeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status only """

    serializer_class = PatientGeneralQuestionB04DeleteSerializer
    queryset = PatientGeneralQuestionB04.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()