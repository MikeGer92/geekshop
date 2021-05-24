from django.contrib import admin

from authapp.models import User

# admin.site.register(User)

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','first_name', 'last_name',)
    fields = ('username', ('first_name', 'last_name'), 'email')
    ordering = ('username',)
    search_fields = ('name',)
