from django.db import models


class BaseModel(models.Model):
    date_modified = models.DateField(auto_now_add=True)
    active_status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Company(BaseModel):
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


class Insurance(BaseModel):
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


class InsuranceRepresentative(BaseModel):
    insurance = models.ForeignKey(Insurance, null=True, blank=True, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    phone_1 = models.CharField(max_length=500, null=True, blank=True)
    phone_2 = models.CharField(max_length=500, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class PatientContact(BaseModel):
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


class PatientAddress(BaseModel):
    patient_contact = models.ForeignKey(PatientContact, null=True, blank=True, on_delete=models.PROTECT)
    address_1 = models.TextField()
    address_2 = models.TextField()
    city = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True, blank=True)
    zip_code = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "%s %s" % (self.patient_contact, self.address_1)        


class PatientPhone(BaseModel):
    PHONE_TYPE = (
        ('Home', 'Home'),
        ('Mobile', 'Mobile'),
        ('Work', 'Work')
    )
    patient_contact = models.ForeignKey(PatientContact, null=True, blank=True, on_delete=models.PROTECT)
    phone = models.CharField(max_length=500, null=True, blank=True)
    phone_type = models.CharField(max_length=500, choices=PHONE_TYPE, null=True, blank=True)
    primary = models.BooleanField(null=True, blank=True, default=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return "%s %s" % (self.patient_contact, self.phone)




