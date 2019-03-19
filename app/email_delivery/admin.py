from django.contrib import admin
from .models import EmailDelivery


@admin.register(EmailDelivery)
class EmailDeliveryAdmin(admin.ModelAdmin):
    search_fields = (
        'book_title',
        'book_id'
    )

    list_display = (
        'user',
        'book_id',
        'book_title',
        'status',
        'send_email',
        'create_at'
    )
