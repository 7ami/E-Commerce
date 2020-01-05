from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Product
from .models import Contact, Checkout


@admin.register(Product, Contact, Checkout)
class ViewAdmin(ImportExportModelAdmin):
    pass
