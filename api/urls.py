from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.resources.appointment_b00 import AppointmentB00ViewSet, AppointmentB00DeleteView
from api.resources.company import CompanyB00ViewSet, CompanyB00DeleteView
from api.resources.insurance import InsuranceB00ViewSet, InsuranceB00DeleteView
from api.resources.insurance_rep import InsuranceB01ViewSet, InsuranceB01DeleteView
from api.resources.organization_m00 import OrganizationM00ViewSet, OrganizationM00DeleteView
from api.resources.organization_location_m01 import OrganizationLocationM01ViewSet, OrganizationLocationM01DeleteView
from api.resources.organization_location_room_m02 import OrganizationLocationRoomM02ViewSet, OrganizationLocationRoomM02DeleteView
from api.resources.organization_staff_m03 import OrganizationStaffM03ViewSet, OrganizationStaffM03DeleteView
from api.resources.patient_address import PatientAddressB01ViewSet, PatientAddressB01DeleteView
from api.resources.patient_contact import PatientContactB00ViewSet, PatientContactB00DeleteView
from api.resources.patient_phone import PatientPhoneB02ViewSet, PatientPhoneB02DeleteView
from api.resources.patient_family_b05 import PatientFamilyB05ViewSet, PatientFamilyB05DeleteView
from api.resources.patient_family_b05s import PatientFamilyB05SViewSet, PatientFamilyB05SDeleteView
from api.resources.patient_general_question_b04 import PatientGeneralQuestionB04ViewSet, PatientGeneralQuestionB04DeleteView
from api.resources.patient_general_question_b04s import PatientGeneralQuestionB04SViewSet, PatientGeneralQuestionB04SDeleteView
from api.resources.patient_general_question_category import PatientGeneralQuestionsCategoryB04RViewSet, PatientGeneralQuestionsCategoryB04RDeleteView
from api.resources.patient_growth_b06 import PatientGrowthB06ViewSet, PatientGrowthB06DeleteView
from api.resources.patient_history_b07 import PatientHistoryB07ViewSet, PatientHistoryB07DeleteView
from api.resources.patient_sibling_b03 import PatientSiblingB03ViewSet, PatientSiblingB03DeleteView
from api.resources.patient_medication_route_b08r1 import PatientMedicationRouteB08R1ViewSet, PatientMedicationRouteB08R1DeleteView
from api.resources.patient_medication_frequency_b08r2 import PatientMedicationFrequencyB08R2ViewSet, PatientMedicationFrequencyB08R2DeleteView
from api.resources.patient_medication_b08 import PatientMedicationB08ViewSet, PatientMedicationB08DeleteView



router = DefaultRouter()

router.register("appointment", AppointmentB00ViewSet)
router.register("company", CompanyB00ViewSet)
router.register("insurance", InsuranceB00ViewSet)
router.register("insurance-rep", InsuranceB01ViewSet)
router.register("organization-m00", OrganizationM00ViewSet)
router.register("organization-location_m01", OrganizationLocationM01ViewSet)
router.register("organization-location-room-m02", OrganizationLocationRoomM02ViewSet)
router.register("organization-staff-m03", OrganizationStaffM03ViewSet)
router.register("patient-address", PatientAddressB01ViewSet)
router.register("patient-contact", PatientContactB00ViewSet)
router.register("patient-phone", PatientPhoneB02ViewSet)
router.register("patient-family-b05", PatientFamilyB05ViewSet)
router.register("patient-family-b05s", PatientFamilyB05SViewSet)
router.register("patient-general-question-b04", PatientGeneralQuestionB04ViewSet)
router.register("patient-general-question-b04s", PatientGeneralQuestionB04SViewSet)
router.register("patient-general-question-category", PatientGeneralQuestionsCategoryB04RViewSet)
router.register("patient-growth-b06", PatientGrowthB06ViewSet)
router.register("patient-history-b07", PatientHistoryB07ViewSet)
router.register("patient-sibling-b03", PatientSiblingB03ViewSet)
router.register("patient-medication-route-b08r1", PatientMedicationRouteB08R1ViewSet)
router.register("patient-medication-frequency-b08r2", PatientMedicationFrequencyB08R2ViewSet)
router.register("patient-medication-b08", PatientMedicationB08ViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("appointmentb00-delete/<int:id>/", AppointmentB00DeleteView.as_view(), name="appointmentb00-delete"),
    path("companyb00-delete/<int:id>/", CompanyB00DeleteView.as_view(), name="companyb00-delete"),
    path("insuranceB00-delete/<int:id>/", InsuranceB00DeleteView.as_view(), name="insuranceb00-delete"),
    path("insuranceB01-delete/<int:id>/", InsuranceB01DeleteView.as_view(), name="insuranceb01-delete"),
    path("organizationm00-delete/<int:id>/", OrganizationM00DeleteView.as_view(), name="organizationm00-delete"),
    path("organization-location-m01-delete/<int:id>/", OrganizationLocationM01DeleteView.as_view(), name="organization-location-m01-delete"),
    path("organization-location-room-m02-delete/<int:id>/", OrganizationLocationRoomM02DeleteView.as_view(), name="organization-location-room-m02-delete"),
    path("organization-staff-m03-delete/<int:id>/", OrganizationStaffM03DeleteView.as_view(), name="organization-staff-m03-delete"),
    path("patient-addressB01-delete/<int:id>/", PatientAddressB01DeleteView.as_view(), name="patient-add-b01-delete"),
    path("patient-contactB00-delete/<int:id>/", PatientContactB00DeleteView.as_view(), name="patient-contact-b00-delete"),
    path("patientPhoneB02-delete/<int:id>/", PatientPhoneB02DeleteView.as_view(), name="patient-phone-b02-delete"),
    path("patient-family-b05-delete/<int:id>/", PatientFamilyB05DeleteView.as_view(), name="patient-family-b05-delete"),
    path("patient-family-b05s-delete/<int:id>/", PatientFamilyB05SDeleteView.as_view(), name="patient-family-b05s-delete"),
    path("patient-general-question-b04-delete/<int:id>/", PatientGeneralQuestionB04DeleteView.as_view(), name="patient-general-question-b04-delete"),
    path("patient-general-question-b04s-delete/<int:id>/", PatientGeneralQuestionB04SDeleteView.as_view(), name="patient-general-question-b04s-delete"),
    path("patient-general-question-category-delete/<int:id>/", PatientGeneralQuestionsCategoryB04RDeleteView.as_view(), name="patient-general-question-category-delete"),
    path("patient-growth-b06-delete/<int:id>/", PatientGrowthB06DeleteView.as_view(), name="patient-growth-b06-delete"),
    path("patient-history-b07-delete/<int:id>/", PatientHistoryB07DeleteView.as_view(), name="patient-history-b07-delete"),
    path("patient-sibling-b03-delete/<int:id>/", PatientSiblingB03DeleteView.as_view(), name="patient-sibling-b03-delete"),
    path("patient-medication-route-b08r1-delete/<int:id>/", PatientMedicationRouteB08R1DeleteView.as_view(), name="patient-medication-route-b08r1-delete"),
    path("patient-medication-frequency-b08r2-delete/<int:id>/", PatientMedicationFrequencyB08R2DeleteView.as_view(), name="patient-medication-frequency-b08r2-delete"),
    path("patient-medication-b08-delete/<int:id>/", PatientMedicationB08DeleteView.as_view(), name="patient-medication-b08-delete"),
]
