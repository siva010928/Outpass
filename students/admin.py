import imp
from django.contrib import admin
from .models import User
from django_object_actions import DjangoObjectActions


# Register your models here.
admin.site.register(User)


class ImportAdmin(DjangoObjectActions, admin.ModelAdmin):
    def imports(modeladmin, request, queryset):
        print("Imports button pushed")

    changelist_actions = ('imports', )