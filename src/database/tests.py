from django.test import TestCase
from api import *

class createDefaultUserTest(TestCase):
	def setUp(self):
		return
	def test_logic(self):
		print type(User.objects.filter(student_id = "1111111111"))
		print len(User.objects.filter(student_id = "1111111111"))
		createDefaultUser();

class hasDefaultUserTest(TestCase):
	def setUp(self):
		return
	def test(self):
		print len(User.objects.filter(student_id = "1111111111"))
		createDefaultQuestionaire()
		print len(User.objects.filter(student_id = "1111111111"))

class createNewQuestionaireTest(TestCase):
	def setUp(self):
		createDefaultUser()

	def test_use(self):
		dict = {
		"act_type" : "vote",
		"time" : "2016",
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
		
class QuestionaireOperateTest(TestCase):
	def setUp(self):
		createSeveralTestQuestionaire()
	def test_delete(self):
		questionaireSet = Questionaire.objects.all()
		print len(questionaireSet)
		dict = {
			"act_id" : 5
		}
		deleteQuestionaire(dict)
		questionaireSet = Questionaire.objects.all()
		print len(questionaireSet)
		for qst in questionaireSet:
			print qst.id

class QuestionOperateTest(TestCase):
	def setUp(self):
		createSeveralQuestions()
	def test_use(self):
		questionSet = Question.objects.all()
		for qst in questionSet:
			print "id = " + str(qst.id) + " order = " + str(qst.question_order)
		dict = {
			"act_id" : 4,
			"qst_id" : 3,
			"operation" : "UP"
		}
		operateQuestion(dict)
		questionSet = Question.objects.all()
		for qst in questionSet:
			print "id = " + str(qst.id) + " order = " + str(qst.question_order)

		dict["operation"] = "DOWN"
		operateQuestion(dict)
		questionSet = Question.objects.all()
		for qst in questionSet:
			print "id = " + str(qst.id) + " order = " + str(qst.question_order)

		dict["operation"] = "REMOVE"
		operateQuestion(dict)
		questionSet = Question.objects.all()
		for qst in questionSet:
			print "id = " + str(qst.id) + " order = " + str(qst.question_order)

class getQuestionaireTest(TestCase):
	"""docstring for getQuestionaireTest"""

		
# Create your tests here.
