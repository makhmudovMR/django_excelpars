from django.contrib import admin
from .models import Municipality, ObjectInfo, Locality, Species


admin.site.register(Municipality)
admin.site.register(ObjectInfo)
admin.site.register(Locality)
admin.site.register(Species)