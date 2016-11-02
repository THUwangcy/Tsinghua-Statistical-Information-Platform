# -*- coding: utf-8 -*-

from models import *
 
def createDefaultUser():
	defaultUser = User(
		student_id = "1111111111",
		real_name = "admin",
		tel = "88888888888",
		email = "default@ggmail.com"
		)
	defaultUser.save()

def hasDefaultUser():
	count = len(User.objects.filter(student_id = "1111111111"))
	if count != 0:
		return True
	return False

def createDefaultQuestionaire():
	dict = {
		"act_type" : "vote",
		"time" : "2016",
		"user_id" : "1111111111"	
		}
	createNewQuestionaire(dict)

def createNewQuestionaire(dict):
	if dict["user_id"] == "1111111111":
		if not hasDefaultUser():
			createDefaultUser()
	TYPE = dict["act_type"]
	switcher = {
		"enroll" : "SU",
		"recruit" : "LW",
		"vote" : "VO"
	}
	currentQuestionaire = Questionaire(
		questionaire_time = dict["time"],
		questionaire_type = switcher[TYPE],
		questionaire_user = User.objects.get(student_id = dict["user_id"])
		)
	currentQuestionaire.save();
	return_dict = {
		"status" : "ok",
		"id" : currentQuestionaire.id
	}
	return return_dict

def createSeveralTestQuestionaire():
	for i in range(10):
		createDefaultQuestionaire()


def saveQuestionaireInfo(dict):
	currentQuestionaire = Questionaire.objects.get(id = dict["act_id"])
	currentQuestionaire.questionaire_title = dict["title"]
	currentQuestionaire.questionaire_introduction = dict["description"]
	currentQuestionaire.save()
	if (currentQuestionaire.questionaire_introduction == dict["description"]) & (currentQuestionaire.questionaire_title == dict["title"]):
		return "ok"
	return "error"

def createNewQuestion(dict):
	print dict["qst_type"]
	thetype = dict["qst_type"]
	switcher = {
		"single" : "SI",
		"multi" : "MU",
		"vote" : "VO",
		"fillin" : "FI",
		"mark" : "MA",
		"sort" : "SO"
	}
	order = len(Question.objects.filter(questionaire_id = dict["act_id"])) + 1
	currentQuestionaire = Questionaire.objects.get(id = dict["act_id"])
	currentQuestionaire.questionaire_numOfQues = currentQuestionaire.questionaire_numOfQues + 1
	currentQuestionaire.save()
	currentQuestion = Question(
		questionaire_id = Questionaire.objects.get(id = dict["act_id"]),
		question_type = switcher[thetype],
		question_order = dict["qst_rank"]
		)

	currentQuestion.save()
	if ((switcher[thetype] == "SI") or (switcher[thetype] == "MU")):
		option1 = Choice(
			question = currentQuestion,
			choice_text = u'选项1',
			choice_order= 1
			)
		option2 = Choice(
			question = currentQuestion,
			choice_text = u'选项2',
			choice_order= 2
			)
		option1.save()
		option2.save()
	return_dict = {
		"status" : "ok",
		"id" : currentQuestion.id
	}
	return return_dict

def createSeveralQuestions():
	createSeveralTestQuestionaire()
	dict = {
		"qst_type" : "single",
		"act_id" : 4,
		"qst_rank" : 1
	}
	for i in range(10):
		dict["qst_rank"] = i
		createNewQuestion(dict)

def createSeveralTestQuestions():
	createSeveralTestQuestionaire()
	dictlist = [{
		"qst_type" : "single",
		"act_id" : 4,
		"qst_rank" : 1
	},
	{
		"qst_type" : "fillin",
		"act_id" : 4,
		"qst_rank" : 2
	},
	{
		"qst_type" : "multi",
		"act_id" : 4,
		"qst_rank" : 1
	}]
	for i in range(12):
		dictlist[i % 3]["qst_rank"] = i + 1
		createNewQuestion(dictlist[i % 3])

def operateQuestion(dict):
	currentQuestion = Question.objects.get(id = dict["qst_id"])
	currentQuestionaire = Questionaire.objects.get(id = dict["act_id"])
	if dict['operation'] == "UP":
		relatedQuestion = Question.objects.get(
			question_order = currentQuestion.question_order - 1,
			questionaire_id__id = dict["act_id"]
			)
		currentQuestion.question_order = currentQuestion.question_order - 1
		relatedQuestion.question_order = relatedQuestion.question_order + 1
		currentQuestion.save()
		relatedQuestion.save()
	if dict['operation'] == "DOWN":
		relatedQuestion = Question.objects.get(
			question_order = currentQuestion.question_order + 1,
			questionaire_id__id = dict["act_id"]
			)
		currentQuestion.question_order = currentQuestion.question_order + 1
		relatedQuestion.question_order = relatedQuestion.question_order - 1
		currentQuestion.save()
		relatedQuestion.save()
	if dict['operation'] == "REMOVE":
		currentQuestionaire = Questionaire.objects.get(id = dict["act_id"])
		currentQuestionaire.questionaire_numOfQues = currentQuestionaire.questionaire_numOfQues - 1
		currentQuestionaire.save()
		relatedQuestionSet = Question.objects.filter(
			question_order__gte = currentQuestion.question_order,
			questionaire_id__id = dict["act_id"]
			)
		currentQuestion.delete()
		for relatedQuestion in relatedQuestionSet:
			relatedQuestion.question_order = relatedQuestion.question_order - 1
			relatedQuestion.save()
	return "ok"

def deleteQuestionaire(dict):
	currentQuestionaire = Questionaire.objects.get(id = dict["act_id"])
	currentQuestionaire.delete()
	return "ok"

def saveQuestionaire(dict):
	currentQuestionaire = Questionaire.objects.get(id = dict["act_id"])
	currentQuestionaire.questionaire_status = "SA"
	currentQuestionaire.save()
	return "ok"

def publishQuestionaire(dict):
	currentQuestionaire = Questionaire.objects.get(id = dict["act_id"])
	currentQuestionaire.questionaire_status = "LA"
	currentQuestionaire.save()
	return "ok"

def getQuestionaireListByStatus(dict):
	switcher  = {
		"pending" : "SA",
		"already" : "LA",
		"all" : "AL"
	}
	if switcher[dict["status"]] == "AL":
		return makeQuestionaireList(Questionaire.objects.exclude(questionaire_status = "IN").filter(questionaire_user__real_name = dict["username"]))
	else:
		return makeQuestionaireList(Questionaire.objects.filter(questionaire_user__real_name = dict["username"]).filter(questionaire_status = switcher[dict["status"]]))

def makeQuestionaireList(List):
	returnList = list()
	for Questionaire in List:
		returnList.append(makeQuestionaireInfo(Questionaire))
	return returnList

def makeQuestionaireInfo(Questionaire):
	status_switcher = {
		"SA" : "pending",
		"LA" : "already",
		"IN" : "new"
	}
	type_switcher = {
		"VO" : "vote",
		"LW" : "recruit",
		"SU" : "enroll"
	}
	dict = {
		"name" : Questionaire.questionaire_title,
		"subscribe_time" : Questionaire.questionaire_time,
		"status" : status_switcher[Questionaire.questionaire_status],
		"type" : type_switcher[Questionaire.questionaire_type],
		"id" : Questionaire.id,
		"description" : Questionaire.questionaire_introduction,
		"fillin" : Questionaire.questionaire_numOfFilled
	}
	return dict

def modifyQuestion(dict):
	currentQuestion = Question.objects.get(id = dict["questions_id"])
	currentQuestion.question_text = dict["qst_title"]
	currentQuestion.save()
	if dict["qst_type"] != "fillin":
		oldChoiceList = Choice.objects.filter(question = currentQuestion)
		for choice in oldChoiceList:
			choice.delete()
		currentQuestion.question_choices = dict["option_num"]
		currentQuestion.save()
		for i in range(int(dict["option_num"])):
			pass_dict = {
				"order" : i + 1,
				"text" : dict["option" + str(i + 1) + "_field"],
				"question_id" : currentQuestion.id
			}
			makeNewChoice(pass_dict)
	else:
		currentQuestion.question_fillinrow = dict["fillin_row"]
		currentQuestion.question_fillincheck = dict["fillin_check"]
		currentQuestion.question_fillinhint = dict["fillin_hint"]
		currentQuestion.save()
	return "ok"

def makeNewChoice(dict):
	currentChoice = Choice(
		choice_order = dict["order"],
		choice_text = dict["text"],
		question = Question.objects.get(id = dict["question_id"])
		)
	currentChoice.save()

def getQuestionaireByID(qid):
	currentQuestionaire = Questionaire.objects.get(id = qid)
	return_dict = dict()
	type_switcher = {
		"VO" : "vote",
		"LW" : "recruit",
		"SU" : "enroll"
	}
	status_switcher = {
		"SA" : "pending",
		"LA" : "already",
		"IN" : "new"
	}
	return_dict["act_type"] = type_switcher[currentQuestionaire.questionaire_type]
	return_dict["act_status"] = status_switcher[currentQuestionaire.questionaire_status]
	return_dict["act_title"] = currentQuestionaire.questionaire_title
	return_dict["act_description"] = currentQuestionaire.questionaire_introduction
	return_dict["qst_num"] = currentQuestionaire.questionaire_numOfQues
	questionList = getQuestionsByQuestionaire(qid)
	return_dict["questions"] = questionList
	return return_dict

def getQuestionsByQuestionaire(qid):
	returnList = list()
	currentQuestionList = Question.objects.filter(questionaire_id__id = qid)
	for question in currentQuestionList:
		currentQuestionDict = makeQuestionDict(question)
		returnList.append(currentQuestionDict)
	return returnList

def makeQuestionDict(qst):
	return_dict = dict()
	type_switcher = {
		"SI" : "single",
		"MU" : "multi",
		"VO" : "vote",
		"FI" : "fillin",
		"MA" : "mark",
		"SO" : "sort"
	}
	return_dict["qst_type"] = type_switcher[qst.question_type]
	return_dict["qst_title"] = qst.question_text
	return_dict["qst_id"] = qst.id
	if qst.question_type == "FI":
		return_dict["rows"] = qst.question_fillinrow
		return_dict["hint"] = qst.question_fillinhint
		return_dict["check"] = qst.question_fillincheck
	else:
		return_dict["option_num"] = qst.question_choices
		optionList = list()
		currentChoices = Choice.objects.filter(question = qst)
		for choice in currentChoices:
			optionList.append("###" + choice.choice_text + "###")
		return_dict["option"] = optionList
	return return_dict
