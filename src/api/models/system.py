from django.db import models
from simple_history.models import HistoricalRecords
from django_currentuser.db.models import CurrentUserField
from django.conf import settings

class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    dateCreated = models.DateTimeField(auto_now_add=True)
    createdBy = CurrentUserField()

    # HISTORY 
    history = HistoricalRecords()

    def __str__(self):
            return ("%s (%s)", self.name, self.dateCreated)

    class Meta:
        ordering = ("dateCreated", 'name', 'pk' )




class Employee(models.Model):
    workId = models.CharField(max_length=20)
    type = models.CharField(max_length=20, 
    choices=settings.EMPLOYEE_TYPES, default=settings.DIGISAVER_SYSTEM_CONFIG['EMPLOYEE_TYPE_DEFAULT'])
    employedDate = models.DateField(auto_now_add=True)
    createdBy = CurrentUserField()

    #RELATIONS
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name = "employee_details"
    )

    branch = models.ForeignKey(Branch, related_name="employees", on_delete = models.DO_NOTHING)

 # HISTORY 
    history = HistoricalRecords()

    def __str__(self):
            return ("%s (%s)", self.workId)

    class Meta:
       ordering = ("workId", 'pk' )