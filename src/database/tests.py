from django.test import TestCase
from api import *

class createDefaultUserTest(TestCase):
	def setUp(self):
		return
	def test_logic(self):
		print type(User.objects.filter(student_id = "1111111111"))
		self.assertEqual(0, len(User.objects.filter(student_id = "1111111111")))
		createDefaultUser();

class hasDefaultUserTest(TestCase):
	def setUp(self):
		return
	def test(self):
		self.assertEqual(0, len(User.objects.filter(student_id = "1111111111")))
		createDefaultQuestionaire()
		self.assertEqual(1, len(User.objects.filter(student_id = "1111111111")))

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
		"qst_rank" : 1
		}
		return_dict = createNewQuestion(dict)
		dict["qst_rank"] = 2
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

class changeQuestionaireStatusTest(TestCase):
	"""docstring for changeQuestionaireStatusTest"""
	def setUp(self):
		createSeveralTestQuestionaire()
	def test_change(self):
		publishQuestionaire({"act_id" : 1})
		publishQuestionaire({"act_id" : 3})
		publishQuestionaire({"act_id" : 5})
		saveQuestionaire({"act_id" : 2})
		saveQuestionaire({"act_id" : 4})
		saveQuestionaire({"act_id" : 6})
		

class getQuestionaireTest(TestCase):
	"""docstring for getQuestionaireTest"""
	def setUp(self):
		createSeveralTestQuestions()

	def test_byStatus(self):
		dict = {
			"status" : "all",
			"username" : 'admin'
		}
		List = getQuestionaireListByStatus(dict)
		for q in List:
			print(q)
		publishQuestionaire({"act_id" : 1})
		publishQuestionaire({"act_id" : 3})
		publishQuestionaire({"act_id" : 5})
		saveQuestionaire({"act_id" : 2})
		saveQuestionaire({"act_id" : 4})
		saveQuestionaire({"act_id" : 6})
		List = getQuestionaireListByStatus(dict)
		for q in List:
			print(q)
		dict["status"] = "pending"
		List = getQuestionaireListByStatus(dict)
		for q in List:
			print(q)
		dict["status"] = "already"
		List = getQuestionaireListByStatus(dict)
		for q in List:
			print(q)

	def test_byID(self):
		for i in range(10):
			r = getQuestionaireByID(i + 1)
			print r


class modifyQuestionTest(TestCase):
	def setUp(self):
		createSeveralTestQuestions()
	def test_single(self):
		dict = {
			"qst_type" : "single",
			"questions_id" : 1,
			"option_num" : 4,
			"qst_title" : "FA Q",
			"option1_field" : "van",
			"option2_field" : "bili",
			"option3_field" : "muji",
			"option4_field" : "mQ"
		}
		modifyQuestion(dict)
		for i in range(10):
			r = getQuestionaireByID(i + 1)
			print r

	def test_getbyID(self):
		dict = {
			"qst_type" : "fillin",
			"questions_id" : 2,
			"qst_title" : "FA Q",
			"fillin_row" : 4,
			"fillin_check" : "picture",
			"fillin_hint" : "philosophy"
		}
		modifyQuestion(dict)
		for i in range(10):
			r = getQuestionaireByID(i + 1)
			print r

class fillQuestionaireTest(TestCase):
	def setUp(self):
		createSeveralTestQuestions()
		dict = {
			"qst_type" : "fillin",
			"questions_id" : 2,
			"qst_title" : "FA Q",
			"fillin_row" : 4,
			"fillin_check" : "picture",
			"fillin_hint" : "philosophy"
		}
		modifyQuestion(dict)
		dict = {
			"qst_type" : "single",
			"questions_id" : 1,
			"option_num" : 4,
			"qst_title" : "FA Q",
			"option1_field" : "van",
			"option2_field" : "bili",
			"option3_field" : "muji",
			"option4_field" : "mQ"
		}
		modifyQuestion(dict)
	def test_fill(self):
		dict = {
			"act_id" : 4,
			"IP" : "0.0.0.0",
			"address" : "beijing",
			"submitTime" : "2016",
			"qst1" : ["option1"],
			"qst2" : "mum",
			"qst3" : ["option1", "option2"]
		}
		fillQuestionaire(dict)
		print (getFillers(4))
		print (getQuestionFill(4, 1, 1))
		print (getQuestionFill(4, 2, 1))
		print (getQuestionFill(4, 3, 1))
	def test_fillSeveral(self):
		dict = {
			"act_id" : 4,
			"IP" : "0.0.0.0",
			"address" : "beijing",
			"submitTime" : "2016",
			"qst1" : ["option1"],
			"qst2" : "mum",
			"qst3" : ["option1", "option2"]
		}
		fillQuestionaire(dict)
		dict = {
			"act_id" : 4,
			"IP" : "0.0.0.1",
			"address" : "beijing",
			"submitTime" : "2017",
			"qst1" : ["option2"],
			"qst2" : "mum?????",
			"qst3" : ["option1", "option2"]
		}
		fillQuestionaire(dict)
		dict = {
			"act_id" : 4,
			"IP" : "0.0.0.2",
			"address" : "beijing",
			"submitTime" : "2018",
			"qst1" : ["option1"],
			"qst2" : "mum",
			"qst3" : ["option1"]
		}
		fillQuestionaire(dict)
		print (getFillers(4))
		print getStatisticsOfQuestion(1)
		print getStatisticsOfQuestion(2)
		print getStatisticsOfQuestion(3)

# Create your tests here.
