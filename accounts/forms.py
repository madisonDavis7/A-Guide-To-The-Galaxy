from allauth.account.forms import SignupForm
from django import forms as d_forms

class ExtendedSignupForm(SignupForm):
	first_name = d_forms.CharField(max_length=30)
	last_name = d_forms.CharField(max_length=30)
	
	def save(self, request):
		user = super(ExtendedSignupForm, self).save(request)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.save()
		return user
