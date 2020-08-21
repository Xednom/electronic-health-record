from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import PatientGeneralQuestionB04S


class PatientGeneralQuestionB04SSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientGeneralQuestionB04S
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientGeneralQuestionB04SDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientGeneralQuestionB04S
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class PatientGeneralQuestionB04SViewSet(viewsets.ModelViewSet):
    queryset = PatientGeneralQuestionB04S.objects.all()
    serializer_class = PatientGeneralQuestionB04SSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class PatientGeneralQuestionB04SDeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status only """

    serializer_class = PatientGeneralQuestionB04SDeleteSerializer
    queryset = PatientGeneralQuestionB04S.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()