from django.contrib import admin
from . import models

# changes what/format used to display the user in the panel
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')

admin.site.register(models.User, UserAdmin)
