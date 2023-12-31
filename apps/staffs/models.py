from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime



class Staff(models.Model):
    STATUS = [("active", "Active"), ("inactive", "Inactive")]
    staff_roll = [("Administrative staff","Administrative staff"),("Acadamic Staff","Acadamic Staff")]
    certificate_choice = [("Aadhar card","Aadhar card"),("Degree certificate","Degree certificate"),("Resume","Resume")]
    GENDER = [("male", "Male"), ("female", "Female")]
    RELIGION_CHOICE = [('Hindu','Hindu'),('Christian','Christian'),('Muslim','Muslim'),("others","others")]
    COMMUNITY_CHOICE = [('OC','OC'),('BC','BC'),('MBC','MBC'),('ST/SC','ST/SC'),("others","others")]
    current_status = models.CharField(max_length=10, choices=STATUS, default="active")
    staff_role = models.CharField("Staff Role",max_length=1024,blank=True,choices=staff_roll)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER, default="male")
    date_of_birth = models.DateField(default=timezone.now)
    date_of_admission = models.DateField("Date of Join",default=timezone.now)
    quali = models.CharField("Qualification",blank=True, max_length=500,null=True)
    study_year = models.IntegerField("If undergoing Year",blank=True,default=None,null=True)
    study_colleg = models.CharField("College Name",max_length=1024,blank=True)
    religion = models.CharField("Religion",max_length=554,default="Hindu",choices=RELIGION_CHOICE)
    community = models.CharField("Community",max_length=524,default="OC", choices=COMMUNITY_CHOICE)
    software_pro = models.CharField("Software Proficiency",max_length=255,blank=True)
    last_salary = models.CharField("Last Job Salary drawn",max_length=255,blank=True)
    working_exp = models.TextField("Working Experience",blank=True,null=True)
    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True
    )
    email = models.EmailField("Email", blank=False, default="")


    address = models.CharField("Address", max_length=255,default=None,blank=True)
    address1 = models.CharField("Address Line 2", max_length=255,default=None,blank=True,null=True)
    address2 = models.CharField("Address Line 3", max_length=255,default=None,blank=True,null=True)
    taluka = models.CharField("Taluk",max_length=255,null=True,default=None,blank=True)
    district = models.CharField("District",max_length=255,default="",blank=True)
    pincode = models.IntegerField("Pincode", blank=True, default=None)
    passport = models.ImageField("Photo",blank=True, upload_to="staff/certificates/")
    aadhar_card = models.ImageField("Aadhar Card",blank=True, upload_to="staff/certificates/")
    degree_certificate = models.ImageField("Degree Certificate",blank=True, upload_to="staff/certificates/")
    resume = models.ImageField("Resume",blank=True, upload_to="staff/certificates/")
    


    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("staff-detail", kwargs={"pk": self.pk})
    def age(self):
        today = datetime.now().date()
        birthdate = self.date_of_birth
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    