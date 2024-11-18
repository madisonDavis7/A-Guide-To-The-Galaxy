from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import SpaceTraveler




class ManualUserCreationTests(TestCase):
	"""
	Manually verifies that regular users and superusers are created successfully and with the correct fields set.
	"""

	def test_createRegularUser(self):
		eq = self.assertEqual

		User: SpaceTraveler = get_user_model() #type:ignore
		user = User.objects.create_user(
			username='testuser',
			email='testuser@example.com',
			password='testpass1234',
			home_planet=2,
			language='en',
			security_question=0,
			security_answer='Mr. Jenkins'
		)

		eq(user.username, 'testuser')
		eq(user.email, 'testuser@example.com')
		eq(user.home_planet, 2)
		eq(user.language, 'en')
		eq(user.security_question, 0)
		eq(user.security_answer, 'Mr. Jenkins')

		self.assertTrue(user.is_active)
		# make sure they're not a god
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)


	def test_createSuperuser(self):
		eq = self.assertEqual

		User: SpaceTraveler = get_user_model() #type:ignore
		superuser = User.objects.create_superuser(
			username='testsuperuser',
			email='testsuperuser@example.com',
			password='testpass1234',
			home_planet=0,
			language='it',
			security_question=0,
			security_answer='Mrs. Jenkins'
		)

		eq(superuser.username, 'testsuperuser')
		eq(superuser.email, 'testsuperuser@example.com')
		eq(superuser.home_planet, 0)
		eq(superuser.language, 'it')
		eq(superuser.security_question, 0)
		eq(superuser.security_answer, 'Mrs. Jenkins')
		
		self.assertTrue(superuser.is_active)
		# make sure they ARE a god
		self.assertTrue(superuser.is_staff)
		self.assertTrue(superuser.is_superuser)

		


class SignUpFormTests(TestCase):
	"""
	Verify the functionality of the signup form.
	"""

	def test_signupViewExistsAtCorrectUrl(self):
		"""Tests the location of the sign-up form view, verifying that it is at the expected location."""
		response = self.client.get('/accounts/signup/')

		self.assertEqual(response.status_code, 200)


	def test_signupViewName(self):
		response = self.client.get(reverse('signup'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'registration/signup.html')


	def test_signupForm(self):
		response = self.client.post(
			reverse('signup'),
			{
				'username': 'testuser',
				'email': 'testuser@example.com',
				'password1': 'testpass123',
				'password2': 'testpass123',
				'home_planet': 2,
				'language': 'en',
				'security_question': 0,
				'security_answer': 'Mr. Jenkins',
			}
		)

		self.assertEqual(response.status_code, 302)  # this should send you home if successful

		allUserObjects = get_user_model().objects.all()
		self.assertEqual(allUserObjects.count(), 1)  # make sure only one user was created
		self.assertEqual(allUserObjects[0].username, 'testuser')
		self.assertEqual(allUserObjects[0].email, 'testuser@example.com')
