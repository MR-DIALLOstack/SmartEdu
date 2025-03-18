from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Etablissement

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'nom', 'prenom', 'role', 'is_active')
    list_filter = ('role', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informations personnelles', {'fields': ('nom', 'prenom', 'date_naissance', 'adresse', 'telephone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'nom', 'prenom', 'telephone', 'role', 'password1', 'password2')}),
    )
    search_fields = ('email', 'nom', 'prenom')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Etablissement)
