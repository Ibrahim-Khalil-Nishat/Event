from django.contrib import admin
from .models import Dcorporate,Dwedding,Dbirthday,specialupload,Review,register,adminregister

# Register your models here.
admin.site.register(Dcorporate)
admin.site.register(Dwedding)
admin.site.register(Dbirthday)
admin.site.register(specialupload)
admin.site.register(Review)
admin.site.register(register)
admin.site.register(adminregister)
