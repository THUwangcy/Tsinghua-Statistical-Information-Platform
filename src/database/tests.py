from django.test import TestCase
from api import *

class createNewQuestionaireTest(TestCase):
	def setUp(self):
		createDefaultUser()

	def test_use(self):
		dict = {
		"act_type" : "vote",
		"time" : 2016,
		"user_id" : "1111111111"	
		}
		return_dict = createNewQuestionaire(dict)
		return_dict = createNewQuestionaire(dict)
		self.assertEqual(return_dict["status"], "ok")
		self.assertEqual(return_dict["id"], 2)
		

# Create your tests here.
