from django.contrib import admin
from .models import Complaints,Villagename

# Register your models here.
admin.site.register(Villagename),
admin.site.register(Complaints)
