from django.contrib import admin
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from .models import Producer,ProducerVerify
# Register your models here.



class ProducerAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'lastName', 'email', 'verified')
    list_filter = ('verified',)  # Add filter for verification status
    actions = ['mark_verified', 'mark_unverified']  # Custom actions for marking producers as verified or unverified

    def mark_verified(self, request, queryset):
        queryset.update(verified=True)
    mark_verified.short_description = 'Mark selected producers as verified'

    def mark_unverified(self, request, queryset):
        queryset.update(verified=False)
    mark_unverified.short_description = 'Mark selected producers as unverified'

    def save_model(self, request, obj, form, change):
        # Call the parent class's save_model method to save the changes
        super().save_model(request, obj, form, change)
        
        # Check if the 'verified' field is in the changed_data list
        if 'verified' in form.changed_data:
            if obj.verified:
                # Send email if verified status changed to True
                verification_url = request.build_absolute_uri(reverse('loginCreation'))
                subject = 'Set up Username and Password'
                message = f'Please click on the following link to verify your account: {verification_url}'
                recipient_email = obj.email
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])


admin.site.register(ProducerVerify,ProducerAdmin)
admin.site.register(Producer)