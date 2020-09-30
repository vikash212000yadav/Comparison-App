from django.db import models

"""
class FilterChoices(models.Model):
    # company = models.TextField(null=True, verbose_name="Company", )
    chipset = models.TextField(null=True, verbose_name="Product", )
    benchmark = models.TextField(null=True, verbose_name="Parameter", )
    values = models.TextField(null=True, verbose_name="Values", )
"""


class Chipset(models.Model):
    chipset_name = models.TextField(null=True, verbose_name="Product", )

    def __str__(self):
        return self.chipset_name


class Benchmark(models.Model):
    benchmark_name = models.TextField(null=True, verbose_name="Parameter")

    def __str__(self):
        return self.benchmark_name


class FilterValue(models.Model):
    chipset = models.ForeignKey(Chipset, on_delete=models.CASCADE)
    benchmark = models.ForeignKey(Benchmark, on_delete=models.CASCADE)
    final_values = models.IntegerField()

    def __str__(self):
        return '%s %s' % (str(self.chipset), str(self.benchmark))


#     def __str__(self):
 #        return str(self.values)

"""
    Chipset
B1    1
B2    2
B3    3
B4    4
B5    5
"""