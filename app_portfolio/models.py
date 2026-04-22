from django.db import models
from django.utils.translation import get_language


class Proyecto(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título (ES)")
    titulo_en = models.CharField(max_length=100, blank=True, verbose_name="Título (EN)")

    descripcion = models.TextField(max_length=500, verbose_name="Descripción (ES)")
    descripcion_en = models.TextField(max_length=500, blank=True, verbose_name="Descripción (EN)")

    tecnologia = models.CharField(
        max_length=120,
        help_text="Separá varias tecnologías con comas. Ej: Python, Django, PostgreSQL",
        verbose_name="Tecnología (ES)",
    )
    tecnologia_en = models.CharField(
        max_length=120,
        blank=True,
        help_text="Opcional. Si se deja vacío, se usa la versión en español.",
        verbose_name="Tecnología (EN)",
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    enlace_github = models.URLField(max_length=200, blank=True)
    enlace_demo = models.URLField(max_length=200, blank=True, null=True)
    imagen_url = models.URLField(max_length=200, blank=True)
    destacado = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.titulo

    # ---- Helpers de traducción ----
    def _tr(self, field_es, field_en):
        """Devuelve el campo en el idioma activo. Fallback a ES si EN está vacío."""
        if get_language() == 'en':
            val = getattr(self, field_en, '')
            return val if val else getattr(self, field_es, '')
        return getattr(self, field_es, '')

    @property
    def titulo_actual(self):
        return self._tr('titulo', 'titulo_en')

    @property
    def descripcion_actual(self):
        return self._tr('descripcion', 'descripcion_en')

    @property
    def tecnologia_actual(self):
        return self._tr('tecnologia', 'tecnologia_en')

    def tecnologias_lista(self):
        """Lista de tecnologías en el idioma activo."""
        return [t.strip() for t in (self.tecnologia_actual or '').split(',') if t.strip()]


class Experiencia(models.Model):
    TIPO_CHOICES = [
        ('trabajo', 'Trabajo'),
        ('educacion', 'Educación'),
        ('certificacion', 'Certificación'),
        ('proyecto', 'Proyecto'),
    ]

    empresa = models.CharField(max_length=100, verbose_name="Empresa (ES)")
    empresa_en = models.CharField(max_length=100, blank=True, verbose_name="Empresa (EN)")

    cargo = models.CharField(max_length=100, verbose_name="Cargo (ES)")
    cargo_en = models.CharField(max_length=100, blank=True, verbose_name="Cargo (EN)")

    descripcion = models.TextField(max_length=500, verbose_name="Descripción (ES)")
    descripcion_en = models.TextField(max_length=500, blank=True, verbose_name="Descripción (EN)")

    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='trabajo')

    class Meta:
        ordering = ['-fecha_inicio']
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"

    def __str__(self):
        return f"{self.cargo} en {self.empresa}"

    def esta_actual(self):
        return self.fecha_fin is None

    # ---- Helpers de traducción ----
    def _tr(self, field_es, field_en):
        if get_language() == 'en':
            val = getattr(self, field_en, '')
            return val if val else getattr(self, field_es, '')
        return getattr(self, field_es, '')

    @property
    def cargo_actual(self):
        return self._tr('cargo', 'cargo_en')

    @property
    def empresa_actual(self):
        return self._tr('empresa', 'empresa_en')

    @property
    def descripcion_actual(self):
        return self._tr('descripcion', 'descripcion_en')


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(max_length=100)
    mensaje = models.TextField(max_length=500)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha_envio']
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"

    def __str__(self):
        return f"Mensaje de {self.nombre} ({self.correo_electronico})"
