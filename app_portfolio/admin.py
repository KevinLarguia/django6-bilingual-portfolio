from django.contrib import admin
from .models import Proyecto, Experiencia, MensajeContacto


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tecnologia', 'destacado', 'tiene_en', 'fecha_creacion')
    list_filter = ('destacado', 'fecha_creacion')
    search_fields = ('titulo', 'tecnologia', 'descripcion')
    list_editable = ('destacado',)
    date_hierarchy = 'fecha_creacion'

    fieldsets = (
        ('🇦🇷 Contenido en español', {
            'fields': ('titulo', 'descripcion', 'tecnologia'),
        }),
        ('🇬🇧 Contenido en inglés (opcional)', {
            'classes': ('collapse',),
            'fields': ('titulo_en', 'descripcion_en', 'tecnologia_en'),
            'description': 'Si dejás estos campos vacíos, se mostrará la versión en español cuando el idioma sea inglés.',
        }),
        ('Enlaces e imagen', {
            'fields': ('enlace_github', 'enlace_demo', 'imagen_url'),
        }),
        ('Configuración', {
            'fields': ('destacado',),
        }),
    )

    def tiene_en(self, obj):
        return bool(obj.titulo_en and obj.descripcion_en)
    tiene_en.boolean = True
    tiene_en.short_description = 'EN'


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'tipo', 'tiene_en', 'fecha_inicio', 'fecha_fin')
    list_filter = ('tipo', 'fecha_inicio')
    search_fields = ('cargo', 'empresa', 'descripcion')
    date_hierarchy = 'fecha_inicio'

    fieldsets = (
        ('🇦🇷 Contenido en español', {
            'fields': ('cargo', 'empresa', 'descripcion'),
        }),
        ('🇬🇧 Contenido en inglés (opcional)', {
            'classes': ('collapse',),
            'fields': ('cargo_en', 'empresa_en', 'descripcion_en'),
            'description': 'Si dejás estos campos vacíos, se mostrará la versión en español cuando el idioma sea inglés.',
        }),
        ('Fechas y tipo', {
            'fields': ('fecha_inicio', 'fecha_fin', 'tipo'),
        }),
    )

    def tiene_en(self, obj):
        return bool(obj.cargo_en and obj.descripcion_en)
    tiene_en.boolean = True
    tiene_en.short_description = 'EN'


@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo_electronico', 'fecha_envio', 'leido')
    list_filter = ('leido', 'fecha_envio')
    search_fields = ('nombre', 'correo_electronico', 'mensaje')
    list_editable = ('leido',)
    readonly_fields = ('fecha_envio',)
    date_hierarchy = 'fecha_envio'


admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Panel de Administración"
