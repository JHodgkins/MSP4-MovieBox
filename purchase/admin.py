"""
import admin so that admin interface can be targated.
import Order and Line item order so that they can be customised .
"""
from django.contrib import admin
from .models import Order, LineItemOrder


class LineItemOrderAdminInline(admin.TabularInline):
    """
    Sets read only fields within the inline admin item order process.
    """
    model = LineItemOrder
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Sets readonly fields and display options for when admins
    add orders using the admin dashboard.
    """
    inlines = (LineItemOrderAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
