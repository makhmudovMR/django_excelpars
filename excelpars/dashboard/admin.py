from django.contrib import admin
from .models import Municipality, ObjectInfo, Locality, Species


admin.site.register(Municipality)
admin.site.register(ObjectInfo)
admin.site.register(Locality)
admin.site.register(Species)


'''
@admin.register(ObjectInfo)
class ObjectInfoAdmin(admin.ModelAdmin):
    list_display = ('nativeName','fullAddress',)
    readonly_fields = ['slug']
    list_filter = ['municipality', 'locality','gen_species_appearance']
    search_fields = ['nativeName', 'description', 'fullAddress']
'''