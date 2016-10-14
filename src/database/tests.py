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
		
class createNewQuestionTest(TestCase):
	def setUp(self):
		createDefaultUser()
		createDefaultQuestionaire()

	def test_use(self):
		dict = {
		"act_id" : 1,
		"qst_type" : "single",
		}
		return_dict = createNewQuestion(dict)
		return_dict = createNewQuestion(dict)
		self.assertEqual(return_dict["status"], "ok")
		self.assertEqual(return_dict["id"], 2)

class saveQuestionaireInfoTest(TestCase):
	def setUp(self):
		createDefaultUser()
		createDefaultQuestionaire()

	def test_use(self):
		dict = {
		"act_id" : 1,
		"title" : "title",
		"description" : "description",
		}
		status = saveQuestionaireInfo(dict)
		self.assertEqual(status, "ok")
		
		

# Create your tests here.
