from django.contrib import admin
from unfold.admin import ModelAdmin

@admin.register(MyModel):
class CustomerAdminClass(ModelAdmin):
    pass
