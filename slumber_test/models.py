from django.db import models


class Pizza(models.Model):
    name = models.fields.CharField(max_length=200, unique=True, blank=False)
    for_sale = models.fields.BooleanField()
    max_extra_toppings = models.fields.IntegerField(null=True, blank=False)

    def __unicode__(self):
        return self.name


class PizzaPrice(models.Model):
    pizza = models.ForeignKey(Pizza, null=False, related_name='prices')
    amount = models.fields.DecimalField(decimal_places=2, max_digits=8)
    date = models.fields.DateField()
