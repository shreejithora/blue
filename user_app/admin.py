from django.contrib import admin
from .models import GuideRegisterModel, TouristRegisterModel, LanguageModel

# Register your models here.

admin.site.register(GuideRegisterModel)
admin.site.register(TouristRegisterModel)
admin.site.register(LanguageModel)