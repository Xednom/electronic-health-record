from rest_framework import serializers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from api.models import PatientGeneralQuestionsCategoryB04R


class PatientGeneralQuestionsCategoryB04RSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientGeneralQuestionsCategoryB04R
        fields = "__all__"
        read_only_fields = ["date_modified"]


class PatientGeneralQuestionsCategoryB04RDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientGeneralQuestionsCategoryB04R
        fields = ['active_status']
        read_only_fields = ["date_modified"]


class PatientGeneralQuestionsCategoryB04RViewSet(viewsets.ModelViewSet):
    queryset = PatientGeneralQuestionsCategoryB04R.objects.all()
    serializer_class = PatientGeneralQuestionsCategoryB04RSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']


class PatientGeneralQuestionsCategoryB04RDeleteView(generics.UpdateAPIView):
    """ An Endpoint for changing the active status only """

    serializer_class = PatientGeneralQuestionsCategoryB04RDeleteSerializer
    queryset = PatientGeneralQuestionsCategoryB04R.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active_status = False
        instance.save(update_fields=['active_status'])
        return Response()