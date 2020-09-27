from django.db import models


class FilterChoices(models.Model):
    # company = models.TextField(null=True, verbose_name="Company", )
    chipset = models.TextField(null=True, verbose_name="Product", )
    benchmark = models.TextField(null=True, verbose_name="Parameter", )
    values = models.TextField(null=True, verbose_name="Values", )



