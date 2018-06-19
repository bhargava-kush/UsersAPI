from django.db import models
import os
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.safestring import mark_safe


# Create your models here.
class UsersData(models.Model):
    full_name = models.CharField(max_length=20,null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True)
    email = models.EmailField()
    emp_code = models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(max_length=10, choices=settings.STATUSES, default=settings.STATUSES[0][0])
    crd = models.DateTimeField(auto_now_add=True)
    upd = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product', blank=True)
    objects = models.Manager()  # The default manager.

    class Meta:
        db_table = 'user_data'


    def __str__(self):
        return self.full_name

    def url(self):
        return os.path.join('/', settings.MEDIA_URL, os.path.basename(str(self.image)))

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

