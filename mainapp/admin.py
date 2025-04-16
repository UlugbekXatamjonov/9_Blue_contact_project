from django.contrib import admin

# Register your models here.

from .models import Contact


@admin.register(Contact)
class Contact_Admin(admin.ModelAdmin):
    list_display = ('full_name', "school", 'grade', 'created_on') # list ko'rinishida ekranga nimalar ko'rinishi
    list_filter = ('school', 'grade', 'created_on') # Qaysi maydonlar filterlanishi
    search_fields = ('full_name', 'school', 'grade', 'phone_number') # Qaysi maydonlarni qidirish mumkinligi







