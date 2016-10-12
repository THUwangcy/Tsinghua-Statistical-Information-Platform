from models import *
 
def createDefaultUser():
	defaultUser = User(
		student_id = "1111111111",
		real_name = "default",
		tel = "88888888888",
		email = "default@ggmail.com"
		)
	defaultUser.save()

def createDefaultQuestionaire():
	defaultQuestionaire = Questionaire(
		questionaire_time = 2016,
		questionaire_type = "VO",
		questionaire_user = User.objects.get(student_id = "1111111111")
		)
	defaultQuestionaire.save()

def createNewQuestionaire(dict):
	TYPE = dict["act_type"]
	switcher = {
		"enroll" : "SU",
		"recuit" : "LW",
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

def saveQuestionaireInfo(dict):
	currentQuestionaire = Questionaire.objects.get(id = dict["act_id"])
	currentQuestionaire.title = dict["title"]
	currentQuestionaire.introduction = dict["description"]
	currentQuestionaire.save()
	if (currentQuestionaire.introduction == dict["description"]) & (currentQuestionaire.title == dict["title"]):
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
	currentQuestion = Question(
		questionaire_id = Questionaire.objects.get(id = dict["act_id"]),
		questionaire_type = switcher[TYPE]
		)
	currentQuestion.save()
	return_dict = {
		"status" : "ok",
		"id" : currentQuestion.id
	}
	return return_dict