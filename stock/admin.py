from django.contrib import admin

from .models import Stock, Transaction, Price


class PriceAdmin(admin.ModelAdmin):
    list_display = ['date', 'stock']

    class Meta:
        model = Price


admin.site.register(Price, PriceAdmin)


class StockAdmin(admin.ModelAdmin):
    list_display = ['ticker', 'name']

    class Meta:
        model = Stock


admin.site.register(Stock, StockAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['date', 'stock']

    class Meta:
        model = Transaction


admin.site.register(Transaction, TransactionAdmin)
