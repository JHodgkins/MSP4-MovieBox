"""
import admin so that admin interface can be targated.
import Order and Line item order so that they can be customised .
"""
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Sets read only fields within the inline admin item order process.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Sets readonly fields and display options for when admins
    add orders using the admin dashboard.
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
