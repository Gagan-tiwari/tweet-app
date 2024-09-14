from django.contrib import admin
from .models import Tweet
from unfold.admin import ModelAdmin
from unfold.forms import AdminAuthenticationForm, UserChangeForm, UserCreationForm
from django.contrib.admin import register
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.unregister(User)

@register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminAuthenticationForm

class TweetAdmin(ModelAdmin):
    list_display = ('user', 'text', 'created_at', 'updates_at')
    list_filter = ('created_at', 'user')
    list_editable = ('text',)
    fields = ('user', 'text', 'photo')

admin.site.register(Tweet, TweetAdmin)

