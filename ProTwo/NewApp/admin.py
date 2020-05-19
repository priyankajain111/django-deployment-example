from django.contrib import admin
from NewApp.models import Webpage,Topic,AccessRecord

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
