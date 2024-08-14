from django.contrib import admin
from .models import DailyMenu
from import_export.admin import ImportExportModelAdmin


admin.site.register(DailyMenu, ImportExportModelAdmin)


