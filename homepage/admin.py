from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group



# unregister the default UserAdmin class
admin.site.unregister(User)
admin.site.unregister(Group)

# register the custom UserAdmin class


admin.site.register(models.blog)
admin.site.register(models.testmonial)
admin.site.register(models.mainregistration)
admin.site.register(models.registration)
admin.site.register(models.videoTestmonial)
admin.site.register(models.faq)
admin.site.register(models.Vlog)
admin.site.register(models.visasuccess)
admin.site.register(models.companytestmonial)
admin.site.register(models.newsletters)



class universitiesdetail(admin.ModelAdmin):
    list_display = ("name", "Course", "country", "state", "los")
admin.site.register(models.universities,universitiesdetail)
