from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import SpaceTraveler


class SpaceTravelerCreationForm(UserCreationForm):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		for field in SpaceTraveler.REQUIRED_FIELDS:
			self.fields[field].required = True
		

	class Meta:
		model = SpaceTraveler
		fields = [
			'first_name',
			'last_name',
			'username',
			'email', 
			'home_planet',
			'language',
			'security_question',
			'security_answer',
		]
		
		


class SpaceTravelerChangeForm(UserChangeForm):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		for field in SpaceTraveler.REQUIRED_FIELDS:
			self.fields[field].required = True


	class Meta:
		model = SpaceTraveler
		fields = [
			'first_name',
			'last_name',
			'username',
			'email', 
			'age',
			'home_planet',
			'language',
			'bio',
			'security_question',
			'security_answer',
		]
