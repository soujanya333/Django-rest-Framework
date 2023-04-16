from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class EmployeeData(models.Model):
    name = models.CharField(_("Name"), max_length=100, null=True, blank=True)
    email = models.EmailField(_("Email"), null=True, blank=True)
    age = models.IntegerField(_("age"),null=True, blank=True)
    gender = models.CharField(_("gender"), max_length=100, null=True, blank=True)
    phone_no= models.CharField(_("phone_no"),max_length=100,null=True, blank=True)
    regid = models.CharField(_('regid'), max_length=100, null=True, blank=True)
    address_details = models.TextField(_("addressdetails"),null=True, blank=True)
    work_exeperience = models.TextField(_("workexeperience"),null=True, blank=True)
    qualifications= models.TextField(_("qualifications"),null=True, blank=True)
    projects= models.TextField(_("projects"),null=True, blank=True)
    photo = models.TextField(_('photo'),null=True, blank=True)
    
    
    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
        db_table = 'employees'

    def __str__(self):
        return "%s" % self.name
