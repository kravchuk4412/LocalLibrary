from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 'sex', 'is_staff', ]
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('date_of_birth', 'sex')}),
	)
	add_fieldsets = UserAdmin.add_fieldsets + (
		(None, {'fields': ('date_of_birth', 'sex')}),
	)

admin.site.register(CustomUser, CustomUserAdmin)
