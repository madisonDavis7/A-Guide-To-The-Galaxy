import logging

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import SpaceTravelerProfileForm
from .models import SpaceTravelerProfile


class SpaceTravelerProfileCreateView(LoginRequiredMixin, CreateView):
	form_class = SpaceTravelerProfileForm
	login_url = settings.LOGIN_URL
	# redirect_field_name = 'index'
	success_url = reverse_lazy('home')
	template_name = 'profiles/create.html'

	def form_valid(self, form):
		# obj = form.save(commit=False)
		# form.instance.real_account = SpaceTravelerProfile.objects.get(user=self.request.user)
		form.initial['real_account'] = self.request.user
		logging.info(self.request.user)
		# form.save()
		# return HttpResponseRedirect(self.get_success_url())
		return super().form_valid(form)


class SpaceTravelerProfileUpdateView(LoginRequiredMixin, UpdateView):
	model = SpaceTravelerProfile
	# form_class = SpaceTravelerProfileForm
	login_url = settings.LOGIN_URL
	# redirect_field_name = 'index'
	fields = [
		'home_planet', 
		'age', 
		'language', 
		'bio', 
		'security_question', 
		'security_answer',
	]
	success_url = reverse_lazy('home')
	template_name = 'profiles/update.html'


class SpaceTravelerProfileViewView(DetailView):
	model = SpaceTravelerProfile
	template_name = 'profiles/view.html'
