from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import SpaceTraveler
from .forms import SpaceTravelerCreationForm, SpaceTravelerChangeForm


@admin.register(SpaceTraveler)
class TutorUserAdmin(UserAdmin):
	# creation
	add_form = SpaceTravelerCreationForm
	# modification
	form = SpaceTravelerChangeForm

	# model = SpaceTraveler
	# fields displayed in the user list
	list_display = [
		'first_name',
		'last_name',
		'email', 
		'home_planet',
		'is_staff',
	]
	
	# fields displayed during creation
	add_fieldsets = (
		(
			None,
			{
				"fields": (
					"username", 
					# "usable_password", 
					"password1", "password2",
					'security_question', 'security_answer',
				)
			}
		),
		(
			_("Personal info"), 
			{ "fields": (
				"first_name", "last_name",
				"email", 'age', 
				'language', 'home_planet',
			)}
		),
	)

	# fields displayed during modification
	fieldsets = (
		( 
			None, { "fields": (
				"username", "password",
				'security_question', 'security_answer',
			)},
		),
		( 
			_("Personal info"), 
			{ "fields": (
				"first_name", "last_name", 
				"email", 'age', 
				'language', 'home_planet',
			)},
		),
        (
            _("Permissions"),
            { "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
			)},
        ),
        ( 
			_("Important dates"), 
			{ "fields": (
				"last_login", "date_joined"
			)},
		),
	)
