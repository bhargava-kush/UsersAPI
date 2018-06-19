# Register your models here.
from django.contrib import admin
from . models import UsersData
from django.contrib.auth.admin import UserAdmin

class UserModelAdmin(admin.ModelAdmin):
    list_display = ["email","full_name","crd","image_tag"]
    list_display_links = ["email","crd"]
    list_filter = ["crd","upd"]
    search_fields = ["full_name"]
    readonly_fields = ["image_tag"]
    class Meta:
        model = UsersData


admin.site.register(UsersData,UserModelAdmin)



