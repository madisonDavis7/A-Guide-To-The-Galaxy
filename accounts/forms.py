from allauth.account.forms import SignupForm
# from allauth.account.forms import ResetPasswordForm
from allauth.account.forms import ResetPasswordKeyForm
from django import forms as d_forms

from django.contrib import messages 

from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
from profiles.models import SpaceTravelerProfile

class ExtendedSignupForm(SignupForm):
	first_name = d_forms.CharField(max_length=30)
	last_name = d_forms.CharField(max_length=30)
	
	def save(self, request):
		user = super(ExtendedSignupForm, self).save(request)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.save()
		return user


class SecurityQuestionResetPasswordKeyForm(ResetPasswordKeyForm):
	security_answer = d_forms.CharField(max_length=30)

	def is_valid(self):
		base_valid = super().is_valid()

		profile = SpaceTravelerProfile.objects.get(real_account=self.user)

		if self.cleaned_data['security_answer'].strip().lower() != profile.security_answer.strip().lower(): #type:ignore
			self.add_error('security_answer', ValidationError('Security answer does not match.'))
			return False

		return base_valid
