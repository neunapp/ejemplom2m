from django.db import models


class Habilidades(models.Model):
    hablidad = models.CharField('Habilidad', max_length=50)

    class meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
    
    def __str__(self):
        return str(self.id) + '-' + self.hablidad



# Create your models here.
class Empleado(models.Model):
    """ Modelo para tabla empleado """

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres completos',
        max_length=120,
        blank=True
    )
    job = models.CharField(
        'Trabajo', 
        max_length=1, 
        choices=JOB_CHOICES
    )
    habilidades = models.ManyToManyField(
        Habilidades,
        through='HabilidadEmpleado',
        blank=True,
    )

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name', 'last_name']


    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name


class HabilidadEmpleado(models.Model):
    habilidades = models.ForeignKey(
        Habilidades, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    empleado = models.ForeignKey(
        Empleado, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    description = models.CharField(
        'descripcion',
        max_length=100,
        blank=True,
    )

    class meta:
        db_table = 'empleado_empleado_habilidades'
        verbose_name = 'Habilidad Empleado'
        verbose_name_plural = 'Habilidades Empleados'
    
    def __str__(self):
        return str(self.id) + '-' + self.empleado.first_name