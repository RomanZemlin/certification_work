from django.contrib import admin

from factory.models import Factory, RetailNetwork, IndividualEntrepreneur, Product

# Register your models here.


class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city')
    list_filter = ('country', 'city')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'supplier', 'debt_to_supplier', 'created_at')
    list_filter = ('supplier__city',)
    actions = ['clear_debt']

    def clear_debt(modeladmin, request, queryset):
        queryset.update(debt_to_supplier=0)

    clear_debt.short_description = "Очистить задолженность"


class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city')
    list_filter = ('country', 'city')
    list_display_links = ('name',)


class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city')
    list_filter = ('country', 'city')
    list_display_links = ('name',)


admin.site.register(Factory, FactoryAdmin)
admin.site.register(RetailNetwork, RetailNetworkAdmin)
admin.site.register(IndividualEntrepreneur, IndividualEntrepreneurAdmin)
admin.site.register(Product, ProductAdmin)
