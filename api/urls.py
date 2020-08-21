from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.resources.company import CompanyB00ViewSet, CompanyB00DeleteView
from api.resources.insurance import InsuranceB00ViewSet, InsuranceB00DeleteView
from api.resources.insurance_rep import InsuranceB01ViewSet, InsuranceB01DeleteView
from api.resources.patient_address import PatientAddressB01ViewSet, PatientAddressB01DeleteView
from api.resources.patient_contact import PatientContactB00ViewSet, PatientContactB00DeleteView
from api.resources.patient_phone import PatientPhoneB02ViewSet, PatientPhoneB02DeleteView


router = DefaultRouter()

router.register("company", CompanyB00ViewSet)
router.register("insurance", InsuranceB00ViewSet)
router.register("insurance-rep", InsuranceB01ViewSet)
router.register("patient-address", PatientAddressB01ViewSet)
router.register("patient-contact", PatientContactB00ViewSet)
router.register("patient-phone", PatientPhoneB02ViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("companyb00-delete/<int:id>/", CompanyB00DeleteView.as_view(), name="companyb00-delete"),
    path("InsuranceB00-delete/<int:id>/", InsuranceB00DeleteView.as_view(), name="insuranceb00-delete"),
    path("InsuranceB01-delete/<int:id>/", InsuranceB01DeleteView.as_view(), name="insuranceb01-delete"),
    path("PatientAddressB01-delete/<int:id>/", PatientAddressB01DeleteView.as_view(), name="patient-add-b01-delete"),
    path("PatientContactB00-delete/<int:id>/", PatientContactB00DeleteView.as_view(), name="patient-contact-b00-delete"),
    path("PatientPhoneB02-delete/<int:id>/", PatientPhoneB02DeleteView.as_view(), name="patient-phone-b02-delete"),
]
