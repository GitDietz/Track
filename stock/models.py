from django.db import models
from django.urls import reverse

# ## Model Managers ## #


# ## Models -  ## #
class Stock(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    note = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.ticker.upper() + " : " + self.name.title()


class Transaction(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    addition = models.FloatField(default=0.0)
    cost_add = models.FloatField(default=0.0)
    holding = models.FloatField(default=0.0)  # this is the total holding at the last transaction date
    holding_cost = models.FloatField(default=0.0)  # this is total holding cost at last transaction

    def __str__(self):
        return self.stock.name


class Price(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    close = models.FloatField(default=0.0)
    value = models.FloatField(default=0.0)

    def __str__(self):
        return self.stock.name

