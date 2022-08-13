import decimal

from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=155, blank=False)
    cnpj = models.CharField(max_length=18, blank=False)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    category = models.CharField(max_length=155, blank=False)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category


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
        max_digits=9, decimal_places=5, default=None
    )
    input_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def output_value(self):
        return round(
            decimal.Decimal(self.input_value * 2), 2
        )
