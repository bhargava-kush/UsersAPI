from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class UsersData(models.Model):
    full_name = models.CharField(max_length=20,null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True)
    email = models.EmailField()
    emp_code = models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(max_length=10, choices=settings.STATUSES, default=settings.STATUSES[0][0])
    crd = models.DateTimeField(auto_now_add=True)
    upd = models.DateTimeField(auto_now=True)
    objects = models.Manager()  # The default manager.

    class Meta:
        db_table = 'user_data'


    def __str__(self):
        return self.full_name