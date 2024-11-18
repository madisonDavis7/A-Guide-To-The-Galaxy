import logging

from django.conf import settings
from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, AccessMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from .forms import SpaceTravelerProfileForm
from .models import SpaceTravelerProfile


class SpaceTravelerProfileCreateView(LoginRequiredMixin, CreateView):
	form_class = SpaceTravelerProfileForm
	login_url = settings.LOGIN_URL
	# redirect_field_name = 'index'
	success_url = reverse_lazy('home')
	template_name = 'profiles/create.html'

	def form_valid(self, form):
		obj = form.save(commit=False)
		# form.real_account = SpaceTravelerProfile.objects.get(real_account=self.request.user)
		form.initial['real_account'] = self.request.user
		# logging.info(self.request.user)
		form.save()
		# return HttpResponseRedirect(self.get_success_url())
		return super().form_valid(form)


class SpaceTravelerProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, AccessMixin, UpdateView):
	model = SpaceTravelerProfile
	form_class = SpaceTravelerProfileForm
	login_url = settings.LOGIN_URL

	success_url = reverse_lazy('home')
	template_name = 'profiles/update.html'

	permission_denied_message = "You cannot edit other user's profiles."

	# def handle_no_permission(self):
	# 	return redirect('home')

	def test_func(self, *args, **kwargs) -> bool:
		"""Function used by UserPassesTestMixin. Used to verify ownership of the profile to update is of the user."""
		# return super().test_func()
		thisModel = super().get_object(*args, **kwargs)
		return thisModel.real_account == self.request.user #type:ignore


class SpaceTravelerProfileViewView(DetailView):
	model = SpaceTravelerProfile
	template_name = 'profiles/view.html'



class SpaceTravelerProfilesListView(ListView):
	model = SpaceTravelerProfile
	template_name = 'profiles/all.html'