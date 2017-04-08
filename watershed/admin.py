from django.contrib import admin
from .models import Watershed,ffInfo,FloraFauna,Maintenance,ManmadeFeature,NaturalFeature,Observation

admin.site.register(Watershed)
admin.site.register(ffInfo)
admin.site.register(FloraFauna)
admin.site.register(Maintenance)
admin.site.register(ManmadeFeature)
admin.site.register(NaturalFeature)
admin.site.register(Observation)
