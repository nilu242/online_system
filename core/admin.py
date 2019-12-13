from django.urls import reverse
from django.contrib import admin
from django.http import HttpRequest
from django.core.mail import send_mail
from django.middleware.csrf import get_token


from allauth.account.views import PasswordResetView


from .models import User


class UserDisp(admin.ModelAdmin):

    list_display = ['email', 'mobile_number', 'role']

    def save_model(self, request, obj, form, change):
        obj.role = 'admin'

        super(UserDisp, self).save_model(request, obj, form, change)

        request.POST = {
            'email': obj.email,
            'csrfmiddlewaretoken': get_token(HttpRequest())
        }

        PasswordResetView.as_view()(request)


admin.site.register(User, UserDisp)
