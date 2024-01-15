from django.contrib import admin

# Register your models here.
from .models import Hospital,Department,Patient
#from . models import Visited

# Register the Hospital model for admin interface
admin.site.register(Hospital)
admin.site.register(Department)
admin.site.register(Patient)
#admin.site.register(Visited)