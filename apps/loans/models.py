import datetime
from secrets import choice
from django.db import models

class VisibleManager(models.Manager):
	def get_queryset(self):
		return super(VisibleManager, self).get_queryset().filter(visible=True)


# Create your models here.
class ActiveInactive(models.Model):
    visible = models.BooleanField(default=True, editable=False)
    deleted_at = models.DateTimeField(blank=True, editable=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Ingreso')

    class Meta:
        abstract = True

    def delete(self):
        self.visible = False
        self.deleted_at = datetime.datetime.now()
        self.save()

class Currency(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    symbol = models.CharField(max_length=20, verbose_name='Símbolo')
    dollar_equivalent = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='Equivalencia en dólares')

    class Meta:
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"

    def __str__(self):
        return self.symbol


class Loan(ActiveInactive):
    amount = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='Monto')
    currency = models.ForeignKey(to='config.Currency', on_delete=models.PROTECT, verbose_name='Moneda')
    period = models.CharField(choices=)
    period_qty = models.IntegerField()

    start_date = models.DateField(verbose_name='Fecha Inicio',)
    is_valid = models.BooleanField(default=True, editable=False, verbose_name='Estado')
    objects = VisibleManager()
    all_objects = models.Manager()
    
    class Meta:
        verbose_name = "Préstamo"
        verbose_name_plural = "Préstamos"

    def __str__(self):
        return 'Contrato No.' + str(self.pk)

    def get_amount_label(self):
        return self.currency.symbol + ' ' + str(self.amount)

    get_amount_label.short_description = 'Monto'

