from django.contrib import admin

from .models import Category, Symptom, Care, Pathology, Resource

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

class SymptomAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

class CareAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    
class PathologyAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

class ResourceAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Symptom, SymptomAdmin)
admin.site.register(Care, CareAdmin)
admin.site.register(Pathology, PathologyAdmin)
admin.site.register(Resource, ResourceAdmin)