from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'email', 'phone_number')
    list_editable = ('email', 'phone_number')
    list_filter = ('gender',)
    list_per_page = 10
    search_fields = ('name', 'gender', 'email', 'phone_number')


admin.site.register(Contact, ContactAdmin)
