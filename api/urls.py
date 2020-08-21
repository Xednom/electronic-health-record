from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.resources.company import CompanyB00ViewSet
from api.resources.insurance import InsuranceB00ViewSet
from api.resources.insurance_rep import InsuranceB01ViewSet
from api.resources.patient_address import PatientAddressB01ViewSet
from api.resources.patient_contact import PatientContactB00ViewSet
from api.resources.patient_phone import PatientPhoneB02ViewSet


router = DefaultRouter()

router.register("company", CompanyB00ViewSet)
router.register("insurance", InsuranceB00ViewSet)
router.register("insurance-rep", InsuranceB01ViewSet)
router.register("patient-address", PatientAddressB01ViewSet)
router.register("patient-contact", PatientContactB00ViewSet)
router.register("patient-phone", PatientPhoneB02ViewSet)

urlpatterns = [path("", include(router.urls))]
