from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.resources.company import CompanyViewSet
from api.resources.insurance import InsuranceViewSet
from api.resources.insurance_rep import InsuranceRepresentativeViewSet
from api.resources.patient_address import PatientAddressViewSet
from api.resources.patient_contact import PatientContactViewSet
from api.resources.patient_phone import PatientPhoneViewSet


router = DefaultRouter()

router.register("company", CompanyViewSet)
router.register("insurance", InsuranceViewSet)
router.register("insurance-rep", InsuranceRepresentativeViewSet)
router.register("patient_address", PatientAddressViewSet)
router.register("patient-contact", PatientContactViewSet)
router.register("patient-phone", PatientPhoneViewSet)

urlpatterns = [path("", include(router.urls))]
