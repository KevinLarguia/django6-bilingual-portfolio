from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.utils.translation import gettext as _
from .models import Proyecto, Experiencia, MensajeContacto


def home(request):
    # Mostramos los últimos 3 proyectos destacados en la home
    # Proyectos marcados como destacados (si no hay, fallback a los 3 últimos)
    proyectos_destacados = Proyecto.objects.filter(destacado=True).order_by('-fecha_creacion')[:3]
    if not proyectos_destacados.exists():
        proyectos_destacados = Proyecto.objects.all().order_by('-fecha_creacion')[:3]
    total_proyectos = Proyecto.objects.count()
    total_experiencias = Experiencia.objects.count()
    context = {
        'proyectos_destacados': proyectos_destacados,
        'total_proyectos': total_proyectos,
        'total_experiencias': total_experiencias,
    }
    return render(request, 'home.html', context)


def proyectos(request):
    termino_busqueda = (request.GET.get('buscar') or '').strip()
    filtro_tech = (request.GET.get('tech') or '').strip()

    mis_proyectos = Proyecto.objects.all().order_by('-destacado', '-fecha_creacion')

    if termino_busqueda:
        mis_proyectos = mis_proyectos.filter(
            Q(titulo__icontains=termino_busqueda) |
            Q(tecnologia__icontains=termino_busqueda) |
            Q(descripcion__icontains=termino_busqueda)
        )

    if filtro_tech and filtro_tech.lower() != 'todos':
        mis_proyectos = mis_proyectos.filter(tecnologia__icontains=filtro_tech)

    # Lista única de tecnologías (se separan por coma si hay varias)
    todas_las_techs = Proyecto.objects.values_list('tecnologia', flat=True)
    techs_unicas = sorted({
        t.strip()
        for tech_string in todas_las_techs
        for t in (tech_string or '').split(',')
        if t.strip()
    })

    context = {
        'proyectos': mis_proyectos.distinct(),
        'techs_unicas': techs_unicas,
        'termino_busqueda': termino_busqueda,
        'filtro_tech': filtro_tech,
    }
    return render(request, 'proyectos.html', context)


def trayectoria(request):
    mis_experiencias = Experiencia.objects.all().order_by('-fecha_inicio')
    return render(request, 'trayectoria.html', {'experiencias': mis_experiencias})


def contacto(request):
    if request.method == 'POST':
        nombre = (request.POST.get('nombre') or '').strip()
        email = (request.POST.get('email') or request.POST.get('correo_electronico') or '').strip()
        mensaje = (request.POST.get('mensaje') or '').strip()

        if nombre and email and mensaje:
            MensajeContacto.objects.create(
                nombre=nombre,
                correo_electronico=email,
                mensaje=mensaje,
            )
            messages.success(
                request,
                _('¡Gracias %(nombre)s! Tu mensaje fue enviado con éxito. Te responderé pronto.') % {'nombre': nombre}
            )
            return redirect('contacto')
        else:
            messages.error(request, _('Por favor, completá todos los campos.'))

    return render(request, 'contacto.html')
