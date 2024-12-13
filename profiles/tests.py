from django.test import TestCase
from django.urls import reverse
from .apps import get_all_profiles
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


from django.core import mail

import yaml
import json
import re

# Create your tests here.


# NOT USED ANYMORE
# class NewSignUpTests(TestCase):
# 	def test_newUsersRedirectedToCreate(self):
# 		response = self.client.post(
# 			reverse('account_signup'),
# 			{
# 				'username': 'testuser',
# 				'email': 'testuser@example.com',
# 				'password1': 'testpass123',
# 				'password2': 'testpass123',
# 			},
# 			follow=False
# 		)


# 		# dc = str(response.context)
# 		# dcj = json.loads(eval(dc))
# 		# print(type(dc))
# 		# print(dc)
# 		# print(type(dcj))
# 		# print(dcj)

# 		# with open('testout.yml', 'w+') as outf1:
# 		# 	yaml.safe_dump(dc, outf1)

# 		print(response.context)
		
# 		activate_url = response.context.get('activate_url', None)
# 		self.assertIsNotNone(activate_url)

# 		response2 = self.client.post(
# 			activate_url,
# 			{}
# 		)
# 		self.assertEqual(response2.status_code, 302)
# 		self.assertRedirects(response2, '/accounts/login')


# 		# self.assertEqual(response.status_code, 302)
# 		# self.assertRedirects(response, '/accounts/confirm-email/')



# def _signup_confirm_email(testcase: TestCase):
# 	token_regex = r"accounts\/confirm-email\/([A-Za-z0-9:\-]+)\/"
# 	hostname = 'testserver'  # this is a test, so we can assume this is true
# 	email_content = mail.outbox[0].body
# 	# print(email_content)
# 	match = re.search(token_regex, email_content)
# 	# assert match.groups(), "Could not find the token in the email"
# 	token = match.group(1)

# 	return testcase.client.post(
# 		'http://' + hostname + '/accounts/confirm-email/' + token,
# 		{'key': token}
# 	)





# class NewProfileTests(TestCase):
# 	def setUp(self):
# 		self.signupResponse = self.client.post(
# 			reverse('account_signup'),
# 			{
# 				'username': 'testuser',
# 				'email': 'testuser@example.com',
# 				'first_name': 'Test',
# 				'last_name': 'User',
# 				'password1': 'testpass123',
# 				'password2': 'testpass123',
# 			}
# 		)

# 		email_confirm_response = _signup_confirm_email(self)
# 		self.assertEqual(email_confirm_response.status_code, 200)

# 		self.client.login(username='testuser', password='testpass123')
# 		self.shouldBe_profileData = {
# 			'home_planet': 2,
# 			'age': 31,
# 			'language': 'en',
# 			'bio': 'am duck',
# 			'security_question': 0,
# 			'security_answer': 'Bob',
# 		}


# 	def test_profileCreation(self):
# 		eq = self.assertEqual

# 		allUserObjects = get_user_model().objects.all()
# 		eq(allUserObjects.count(), 1)  # make sure only one user was created
# 		eq(allUserObjects[0].username, 'testuser')

# 		response = self.client.post(
# 			reverse('profiles:create'),
# 			self.shouldBe_profileData
# 		)

# 		eq(response.status_code, 302)

# 		allProfileObjects = get_all_profiles().objects.all()
# 		eq(allProfileObjects.count(), 1)
# 		# owned by that user
# 		eq(allProfileObjects[0].real_account.pk, 1) #type:ignore
		
# 		# all data was set correctly
# 		for k in self.shouldBe_profileData.keys():
# 			eq(
# 				getattr(allProfileObjects[0], k),
# 				self.shouldBe_profileData[k]
# 			)
		

# 	def test_profileChange(self):
# 		eq = self.assertEqual

# 		create = self.client.post(
# 			reverse('profiles:create'),
# 			self.shouldBe_profileData
# 		)


# 		changeData = self.shouldBe_profileData
# 		changeData['bio'] = 'am human now'
# 		response = self.client.post(
# 			reverse('profiles:update', kwargs={'pk': 1}),
# 			changeData
# 		)

# 		eq(response.status_code, 302)

# 		allProfileObjects = get_all_profiles().objects.all()
# 		eq(allProfileObjects.count(), 1)
# 		# owned by that user
# 		eq(allProfileObjects[0].real_account.pk, 1) #type:ignore
		
# 		# all data was set correctly
# 		for k in changeData.keys():
# 			eq(
# 				getattr(allProfileObjects[0], k),
# 				changeData[k]
# 			)
