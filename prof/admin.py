from django.contrib import admin
from . models import prof
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address', 'bca', 'mca', 'lang', 'tenth', 'twelth')


admin.site.register(prof, ProfileAdmin)
