from django.db import models


class BaseModel(models.Model):
    date_modified = models.DateField(auto_now_add=True)
    active_status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CompanyB00(BaseModel):
    name = models.CharField(max_length=500, null=True, blank=True)
    address_1 = models.TextField()
    address_2 = models.TextField()
    city = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True, blank=True)
    zip_code = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return "%s" % (self.name)


class InsuranceB00(BaseModel):
    address_1 = models.TextField()
    address_2 = models.TextField()
    city = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True, blank=True)
    zip_code = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=500, null=True, blank=True)

    class Meta: 
        ordering = ["-id"]
    
    def __str__(self):
        return "%s %s" % (self.city, self.state)


class InsuranceB01(BaseModel):
    insurance = models.ForeignKey(InsuranceB00, null=True, blank=True, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    phone_1 = models.CharField(max_length=500, null=True, blank=True)
    phone_2 = models.CharField(max_length=500, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class PatientContactB00(BaseModel):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    CONTACT_TYPE = (
        ('Patient', 'Patient'),
        ('Relative', 'Relative')
    )
    RELATIONSHIP = (
        ('Self', 'Self'),
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Guardian', 'Guardian')
    )
    first_name = models.CharField(max_length=500, null=True, blank=True)
    middle_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=500, choices=GENDER, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    contact_type = models.CharField(max_length=500, choices=CONTACT_TYPE, null=True, blank=True)
    patient_relationship = models.CharField(max_length=500, choices=RELATIONSHIP, null=True, blank=True)

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return "%s %s" % (self.last_name, self.contact_type)


class PatientAddressB01(BaseModel):
    patient_contact = models.ForeignKey(PatientContactB00, null=True, blank=True, on_delete=models.PROTECT)
    address_1 = models.TextField()
    address_2 = models.TextField()
    city = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True, blank=True)
    zip_code = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "%s %s" % (self.patient_contact, self.address_1)        


class PatientPhoneB02(BaseModel):
    PHONE_TYPE = (
        ('Home', 'Home'),
        ('Mobile', 'Mobile'),
        ('Work', 'Work')
    )
    patient_contact = models.ForeignKey(PatientContactB00, null=True, blank=True, on_delete=models.PROTECT)
    phone = models.CharField(max_length=500, null=True, blank=True)
    phone_type = models.CharField(max_length=500, choices=PHONE_TYPE, null=True, blank=True)
    primary = models.BooleanField(null=True, blank=True, default=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return "%s %s" % (self.patient_contact, self.phone)


class PatientSiblingB03(BaseModel):
    RELATIONSHIP = (
        ("Brother", "Brother"),
        ("Sister", "Sister"),
    )
    patient_contact_b00_rec = models.ForeignKey(PatientContactB00, null=True, blank=True, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=500, null=True, blank=True)
    middle_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    relationship = models.CharField(max_length=500, choices=RELATIONSHIP, null=True, blank=True)
    age = models.CharField(max_length=500, null=True, blank=True)

    class Meta: 
        ordering = ["-id"]
    
    def __str__(self):
        return "%s %s - %s" % (self.last_name, self.first_name, self.relationship)


class PatientGeneralQuestionsCategoryB04R(BaseModel):
    name = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField()

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return "%s %s" % (self.name, self.description)


class PatientGeneralQuestionB04S(BaseModel):
    patient_general_question_category_b04r_rec = models.ForeignKey(PatientGeneralQuestionsCategoryB04R, null=True, blank=True, on_delete=models.PROTECT)
    question = models.TextField()
    question_type = models.CharField(max_length=500, null=True, blank=True)
    question_extended = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return "%s %s" % (self.patient_general_question_category_b04r_rec, self.question_type)


class PatientGeneralQuestionB04(BaseModel):
    patient_general_question_category_b04s_rec = models.ForeignKey(PatientGeneralQuestionB04S, null=True, blank=True, on_delete=models.PROTECT)
    question = models.CharField(max_length=500, null=True, blank=True)
    question_extended = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return "%s %s" % (self.patient_general_question_category_b04s_rec, self.question)


class PatientFamilyB05S(BaseModel):
    question = models.TextField()
    mother = models.BooleanField(default=False)
    mother_side = models.BooleanField(default=False)
    father = models.BooleanField(default=False)
    father_side = models.BooleanField(default=False)
    brother = models.BooleanField(default=False)
    sister = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']
    

class PatientFamilyB05(BaseModel):
    patient_contact_b00_rec = models.ForeignKey(PatientContactB00, null=True, blank=True, on_delete=models.PROTECT)
    question = models.TextField()
    mother = models.BooleanField(default=False)
    mother_side = models.BooleanField(default=False)
    father = models.BooleanField(default=False)
    father_side = models.BooleanField(default=False)
    brother = models.BooleanField(default=False)
    sister = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]


class PatientGrowthB06(BaseModel):
    patient_contact_b00_rec = models.ForeignKey(PatientContactB00, null=True, blank=True, on_delete=models.PROTECT)
    question = models.TextField()
    when = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]


class PatientHistoryB07(BaseModel):
    patient_contact_b00_rec = models.ForeignKey(PatientContactB00, null=True, blank=True, on_delete=models.PROTECT)
    question = models.TextField()
    answer = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ['-id']