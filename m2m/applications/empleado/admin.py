from django.contrib import admin
from .models import Empleado, Habilidades, HabilidadEmpleado
#

class HabilidadEmpleadoInline(admin.TabularInline):
    model = HabilidadEmpleado
    extra = 1
    autocomplete_fields = ['habilidades']


class HabilidadesAdmin(admin.ModelAdmin):
    inlines = (HabilidadEmpleadoInline,)
    search_fields = ('hablidad'),
    ordering = ['hablidad']


class EmpleadoAdmin(admin.ModelAdmin):
    inlines = [HabilidadEmpleadoInline,]
    list_display = (
        'first_name',
        'last_name',
        'job',
        'full_name',
        'id',
    )
    #
    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name
    #
    search_fields = ('first_name',)
    list_filter = ('job', 'habilidades',)
    #
    filter_horizontal = ['habilidades',]


admin.site.register(Habilidades, HabilidadesAdmin)
admin.site.register(Empleado, EmpleadoAdmin)