import models

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
		questionaire_user = dict["user_id"]
		)
	currentQuestionaire.save();
	return_dict = {
		"status" : "ok",
		"id" : currentQuestionaire.id()
	}

	return return_dict

def saveQuestionaireInfo(dict):
	currentQuestionaire = Questionaire.objects.get(id = dict["act_id"])
	currentQuestionaire.title = dict["title"]
	currentQuestionaire.introduction = dict["description"]
	currentQuestionaire.save()
	return "ok"

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
		questionaire_id = dict["act_id"],
		questionaire_type = switcher[TYPE]
		)
	currentQuestion.save()
	return_dict = {
		"status" : "ok",
		"id" : currentQuestion.i
	}
	return return_dict