from django.contrib import admin

# Models
from apps.usuarios.models import Usuario
# Register your models here.

@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    """User admin."""

    list_display = ('id', 'first_name', 'last_name', 'mail',)
    list_display_links = ('id', 'first_name', 'last_name', 'mail',)

    search_fields = (
        'mail',
        'first_name',
        'last_name',
    )

    list_filter = (
        'is_active',
        'is_staff',
        'date_joined',
        'modified',
    )

    readonly_fields = ('date_joined', 'modified',)