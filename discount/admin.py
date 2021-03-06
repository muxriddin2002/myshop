from django.contrib import admin
from .models import Coupon

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount_percent', 'active']
    list_filter = ['active', 'valid_to', 'valid_from']
    search_fields = ['code']

admin.site.register(Coupon, CouponAdmin)
