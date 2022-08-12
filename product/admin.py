from django.contrib import admin

from product.models import Category, Product, Provider


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cnpj',)
    list_display_links = ('name', 'cnpj',)
    list_filter = ('name', 'cnpj',)
    list_editable = ('is_active',)
    list_per_page = 15
    search_fields = ('name', 'cnpj',)
    ordering = ('-id',)
    prepopulated_fields = {"slug": ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    list_display_links = ('category',)
    list_filter = ('category',)
    list_editable = ('is_active',)
    list_per_page = 15
    search_fields = ('category',)
    ordering = ('-id',)
    prepopulated_fields = {"slug": ('category',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    list_display_links = ('name',)
    list_filter = ('name', 'category', 'provider',)
    list_editable = ('is_active',)
    list_per_page = 15
    search_fields = ('name', 'category',)
    ordering = ('-id',)
    prepopulated_fields = {"slug": ('name',)}
