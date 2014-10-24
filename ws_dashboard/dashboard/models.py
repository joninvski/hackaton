from django.db import models

PHONE_INTERACTION_CHOICES = (
    (1, 'INCOMING'),
    (2, 'OUTGOING')
)

COMPANY_ROLES = (
    (1, 'BOSS'),
    (2, 'SUPERBOSS')
)

class Company(models.Model): 
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)    

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Companies"

class Employee(models.Model):
    name = models.CharField(max_length=30)
    role = models.IntegerField(choices=COMPANY_ROLES)
    phone_number = models.CharField(max_length=30)
    company = models.ForeignKey(Company, related_name="employees_company")

    def __unicode__(self):
        return self.name

class Call(models.Model):
    owner = models.ForeignKey(Employee, related_name="calls_employee")
    caller = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    length = models.IntegerField()
    # GPS/Android Information
    call_type = models.IntegerField(choices=PHONE_INTERACTION_CHOICES)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.receiver 

class Message(models.Model): 
    owner = models.ForeignKey(Employee, related_name="messages_employee")
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    sent_time = models.DateTimeField()
    message_type = models.IntegerField(choices=PHONE_INTERACTION_CHOICES)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    
    def __unicode__(self):
        return self.receiver

class Data(models.Model): 
    owner = models.ForeignKey(Employee, related_name="data_employee")
    volume = models.IntegerField(help_text="Amount of kb exchanged")
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    start_time = models.DateTimeField() 
    data_type = models.IntegerField(choices=PHONE_INTERACTION_CHOICES)
    def __unicode__(self):
        return str(self.volume)

    class Meta:
        verbose_name_plural = "Data"

# Create your models here.
