from models import *
 
def createDefaultUser():
	defaultUser = User(
		student_id = "1111111111",
		real_name = "default",
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
	TYPE = dict["qst_type"]
	switcher = {
		"single" : "SI",
		"multi" : "MU",
		"vote" : "VO",
		"fillin" : "FI",
		"mark" : "MA",
		"sort" : "SO"
	}
	order = len(Question.objects.filter(questionaire_id = dict["act_id"])) + 1
	currentQuestion = Question(
		questionaire_id = Questionaire.objects.get(id = dict["act_id"]),
		question_type = switcher[TYPE],
		question_order = dict["qst_rank"]
		)
	currentQuestion.save()
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

def getQuestionaireListByStatus(str):
	switcher  = {
		"pending" : "SA",
		"already" : "LA",
		"all" : "AL"
	}
	if switcher[str] == "AL":
		return makeQuestionaireList(Questionaire.objects.all())
	else:
		return makeQuestionaireList(Questionaire.objects.filter(questionaire_status = switcher[str]))

def makeQuestionaireList(List):
	returnList = list()
	for Questionaire in List:
		returnList.add(makeQuestionaireInfo(Questionaire))
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
