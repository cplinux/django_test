from django.contrib import admin

# Register your models here.

from people import models

admin.site.register(models.People)
