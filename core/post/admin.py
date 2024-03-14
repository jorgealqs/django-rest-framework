from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse
from core.post.models import Post
from core.post.filter.filter import CreatedDateFilter
import csv


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Post"), {
            "fields": (
                "author",
                "body"
            ),
        }),
        (_("Post"), {
            "fields": (
                "edited",
            ),
        }),
    )
    readonly_fields = ("author_name",)  # Campo de solo lectura para mostrar el nombre del autor
    list_display = [
        'author_name',
        'body',
        'created',
        'updated',
        'edited',
    ]
    list_filter = [
        CreatedDateFilter,  # Agrega el filtro por fecha de creación
        'edited'
    ]
    search_fields = [
        'author__first_name',
        'created'  # Habilita la búsqueda por fecha de creación
    ]

    actions = ['download_selected_posts']
    ordering = ["id"]

    def download_selected_posts(self, request, queryset):
        """
        Acción personalizada para descargar los posts seleccionados.
        """
        selected_posts = queryset.values_list('author__first_name', 'body', 'created', flat=False)

        # Una vez que hayas generado el archivo, devuélvelo como una respuesta HTTP
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="selected_posts.csv"'

        # Escribe los datos de los posts en el archivo CSV
        writer = csv.writer(response)
        writer.writerow(['Author', 'Body', 'Created Date'])  # Escribir encabezados
        for post in selected_posts:
            writer.writerow(post)

        return response

    download_selected_posts.short_description = _('Download selected posts')


    def author_name(self, obj):
        return obj.author.first_name if obj.author else None

    author_name.short_description = 'Author'
