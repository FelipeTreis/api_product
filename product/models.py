from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=155, blank=False)
    cnpj = models.CharField(max_length=18, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    category = models.CharField(max_length=155, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    provider = models.ForeignKey(
        Provider, on_delete=models.SET_NULL,
        null=True, blank=True, default=None,
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True, default=None
    )
    input_value = models.DecimalField(
        max_digits=7, decimal_places=2, default=None
    )
    input_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def output_value(self):
        return (self.input_value + (self.input_value * 0.4))
