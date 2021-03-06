# -*- coding: utf-8 -*-

from models import *
import hashlib


def md5encode(act_id):
	m = hashlib.md5()
	m.update(act_id)
	return m.hexdigest()

def createDefaultUser():
	defaultUser = User(
		student_id = "1111111111",
		real_name = "admin",
		tel = "88888888888",
		email = "default@ggmail.com"
		)
	defaultUser.save()

def createUser(dict):
	tryUser = User.objects.filter(username = dict["username"])
	if len(tryUser) != 0:
		return
	newUser = User(
		student_id = dict["user_id"],
		username = dict["username"],
		identity = dict["identity"],
		email = dict["email"],
		real_name = dict["real_name"]
		)
	newUser.save()

def userInfoChange(dict):
	currentUser = User.objects.get(username = dict["username"])
	currentKeys = dict.keys()
	for key in currentKeys:
		if key == "username":
			continue
		if key == "gender":
			currentUser.gender = dict["gender"]
		if key == "status":
			currentUser.status = dict["status"]
		if key == "address":
			currentUser.address = dict["address"]
		if key == "age":
			currentUser.age = dict["age"]
		if key == "telephone_number":
			currentUser.tel = dict["telephone_number"]
		if key == "email":
			currentUser.email = dict["email"]
	currentUser.save()

def getUserInfo(myusername):
	currentUser = User.objects.get(username = myusername)
	return makeUserDict(currentUser)

def makeUserDict(currentUser):
	return_dict = {
		"username" : currentUser.username,
		"user_id" : currentUser.student_id,
		"real_name" : currentUser.real_name,
		"identity" : currentUser.identity,
		"email" : currentUser.email,
		"telephone_number" : currentUser.tel,
		"age" : currentUser.age,
		"gender" : currentUser.gender,
		"status" : currentUser.status,
		"address" : currentUser.address
	}
	return return_dict

def getAllUser():
	userlist = User.objects.all()
	return userlist

def getAllUserInfo():
	userlist = getAllUser()
	return_list = list()
	for user in userlist:
		return_list.append(makeUserDict(user))
	return return_list

def getAllQustionaireInfo():
	userlist = getAllUser()
	return_list = list()
	for user in userlist:
		currentlist = makeQuestionaireList(Questionaire.objects.filter(questionaire_user = user).filter(questionaire_status = "LA"))
		output = open('listview', 'w')
		output.write(str(len(currentlist)))
		output.close()
		for aquestionaire in currentlist:
			aquestionaire["username"] = user.username
		return_list.extend(currentlist)
	return return_list

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
	currentQuestionaire.save()
	currentQuestionaire.questionaire_md5 = md5encode(str(currentQuestionaire.id) + currentQuestionaire.questionaire_time)
	currentQuestionaire.save()
	if currentQuestionaire.questionaire_type == "SU":
		currentQuestionaire.questionaire_title = u"XX活动报名"
		currentQuestionaire.save()
	if currentQuestionaire.questionaire_type == "VO":
		currentQuestionaire.questionaire_title = u"票选最xxxx"
		currentQuestionaire.save()
		dict = {
			"act_id" : currentQuestionaire.questionaire_md5,
			"qst_type" : "vote",
			"qst_rank" : 1
		}
		createNewQuestion(dict)
	if currentQuestionaire.questionaire_type == "LW":
		currentQuestionaire.questionaire_title = u"XX实验志愿者招募"
		currentQuestionaire.save()
		dict = {
			"act_id" : currentQuestionaire.questionaire_md5,
			"qst_type" : "fillin",
			"qst_rank" : 1
		}
		qid = createNewQuestion(dict)["id"]
		mddict = {
			"questions_id" : qid,
			"qst_title" : u"你的名字",
			"fillin_row" : 1,
			"fillin_hint" : "",
			"fillin_check" : u"文本",
			"qst_type" : "fillin",
			"must" : "true"
		}
		modifyQuestion(mddict)
		dict = {
			"act_id" : currentQuestionaire.questionaire_md5,
			"qst_type" : "fillin",
			"qst_rank" : 2
		}
		qid = createNewQuestion(dict)["id"]
		mddict = {
			"questions_id" : qid,
			"qst_title" : u"你的联系方式",
			"fillin_row" : 1,
			"fillin_hint" : "",
			"fillin_check" : u"文本",
			"qst_type" : "fillin",
			"must" : "true"
		}
		modifyQuestion(mddict)
		dict = {
			"act_id" : currentQuestionaire.questionaire_md5,
			"qst_type" : "mark",
			"qst_rank" : 3
		}
		createNewQuestion(dict)
		
	return_dict = {
		"status" : "ok",
		"id" : currentQuestionaire.questionaire_md5
	}
	return return_dict

def createSeveralTestQuestionaire():
	for i in range(10):
		createDefaultQuestionaire()


def saveQuestionaireInfo(dict):
	currentQuestionaire = Questionaire.objects.get(questionaire_md5 = dict["act_id"])
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
	order = len(Question.objects.filter(questionaire_id__questionaire_md5 = dict["act_id"])) + 1
	currentQuestionaire = Questionaire.objects.get(questionaire_md5 = dict["act_id"])
	currentQuestionaire.questionaire_numOfQues = currentQuestionaire.questionaire_numOfQues + 1
	currentQuestionaire.save()
	currentQuestion = Question(
		questionaire_id = Questionaire.objects.get(questionaire_md5 = dict["act_id"]),
		question_type = switcher[thetype],
		question_order = dict["qst_rank"]
		)

	currentQuestion.save()
	if ((switcher[thetype] == "SI") or (switcher[thetype] == "MU") or (switcher[thetype] == "VO") or (switcher[thetype] == "MA")):
		currentQuestion.question_choices = 2
		currentQuestion.save()
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
		if (switcher[thetype] == "MA"):
			option1.choice_text = "10:00-11:00"
			option1.choice_limit = 5
			option2.choice_text = "11:00-12:00"
			option2.choice_limit = 7
		if (switcher[thetype] == "VO"):
			option1.choice_text = u"选项1"
			option2.choice_text = u"选项2"
			option1.choice_hasPicture = False
			option2.choice_hasPicture = False
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
	currentQuestionaire = Questionaire.objects.get(questionaire_md5 = dict["act_id"])
	if dict['operation'] == "UP":
		relatedQuestion = Question.objects.get(
			question_order = currentQuestion.question_order - 1,
			questionaire_id__questionaire_md5 = dict["act_id"]
			)
		currentQuestion.question_order = currentQuestion.question_order - 1
		relatedQuestion.question_order = relatedQuestion.question_order + 1
		currentQuestion.save()
		relatedQuestion.save()
	if dict['operation'] == "DOWN":
		relatedQuestion = Question.objects.get(
			question_order = currentQuestion.question_order + 1,
			questionaire_id__questionaire_md5 = dict["act_id"]
			)
		currentQuestion.question_order = currentQuestion.question_order + 1
		relatedQuestion.question_order = relatedQuestion.question_order - 1
		currentQuestion.save()
		relatedQuestion.save()
	if dict['operation'] == "REMOVE":
		currentQuestionaire = Questionaire.objects.get(questionaire_md5 = dict["act_id"])
		currentQuestionaire.questionaire_numOfQues = currentQuestionaire.questionaire_numOfQues - 1
		currentQuestionaire.save()
		relatedQuestionSet = Question.objects.filter(
			question_order__gte = currentQuestion.question_order,
			questionaire_id__questionaire_md5 = dict["act_id"]
			)
		currentQuestion.delete()
		for relatedQuestion in relatedQuestionSet:
			relatedQuestion.question_order = relatedQuestion.question_order - 1
			relatedQuestion.save()
	return "ok"

def deleteQuestionaire(dict):
	currentQuestionaire = Questionaire.objects.get(questionaire_md5 = dict["act_id"])
	currentQuestionaire.delete()
	return "ok"

def saveQuestionaire(dict):
	currentQuestionaire = Questionaire.objects.get(questionaire_md5 = dict["act_id"])
	currentQuestionaire.questionaire_status = "SA"
	currentQuestionaire.save()
	return "ok"

def publishQuestionaire(dict):
	currentQuestionaire = Questionaire.objects.get(questionaire_md5 = dict["act_id"])
	currentQuestionaire.questionaire_status = "LA"
	currentQuestionaire.save()
	return "ok"

def stopQuestionaire(dict):
	currentQuestionaire = Questionaire.objects.get(questionaire_md5 = dict["act_id"])
	currentQuestionaire.questionaire_status = "PA"
	currentQuestionaire.save()
	return "ok"

def getQuestionaireListByStatus(dict):
	switcher  = {
		"pending" : "SA",
		"already" : "LA",
		"all" : "AL"
	}
	if switcher[dict["status"]] == "AL":
		return makeQuestionaireList(Questionaire.objects.exclude(questionaire_status = "IN").filter(questionaire_user__username = dict["username"]))
	else:
		return makeQuestionaireList(Questionaire.objects.filter(questionaire_user__username = dict["username"]).filter(questionaire_status = switcher[dict["status"]]))


def makeQuestionaireList(List):
	returnList = list()
	for Questionaire in List:
		returnList.append(makeQuestionaireInfo(Questionaire))
	return returnList


def makeQuestionaireInfo(Questionaire):
	status_switcher = {
		"SA" : "pending",
		"LA" : "already",
		"IN" : "new",
		"PA" : "pause"
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
		"id" : Questionaire.questionaire_md5,
		"description" : Questionaire.questionaire_introduction,
		"fillin" : Questionaire.questionaire_numOfFilled
	}
	return dict

def modifyQuestion(dict):
	currentQuestion = Question.objects.get(id = dict["questions_id"])
	currentQuestion.question_text = dict["qst_title"]
	questionKeys = dict.keys()
	if "must" in questionKeys:
		currentQuestion.question_mustfill = True
	else:
		currentQuestion.question_mustfill = False
	currentQuestion.save()
	if dict["qst_type"] != "fillin":
		oldChoiceList = Choice.objects.filter(question = currentQuestion)
		for choice in oldChoiceList:
			choice.delete()
		currentQuestion.question_choices = dict["option_num"]
		if "min_selected" in questionKeys:
			if dict["min_selected"] != "":
				currentQuestion.question_minfill = int(dict["min_selected"])
			else:
				currentQuestion.question_minfill = None
		if "max_selected" in questionKeys:
			if dict["max_selected"] != "":
				currentQuestion.question_maxfill = int(dict["max_selected"])
			else:
				currentQuestion.question_maxfill = None
		if dict["qst_type"] == "vote":
			if "display_vote" in questionKeys:
				currentQuestion.question_displayVotes = True
			if dict["ip_times"] != "":
				currentQuestion.question_ipTimes = int(dict["ip_times"])
			if dict["day_times"] != "":
				currentQuestion.question_dayTimes = int(dict["day_times"])
		currentQuestion.save()
		for i in range(int(dict["option_num"])):
			pass_dict = {
				"order" : i + 1,
				"text" : dict["option" + str(i + 1) + "_field"],
				"question_id" : currentQuestion.id
			}
			if dict["qst_type"] == "vote":
				pass_dict["has_picture"] = dict["option" + str(i + 1) + "_img"]
			else:
				pass_dict["has_picture"] = ""
			if ("option" + str(i + 1) + "_maxium") in questionKeys:
				pass_dict["limit"] = dict["option" + str(i + 1) + "_maxium"]
			else:
				pass_dict["limit"] = ""
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
	if dict["limit"] != "":
		currentChoice.choice_limit = int(dict["limit"])
	if dict["has_picture"] != "":
		if dict["has_picture"] == "true":
			currentChoice.choice_hasPicture = True
		else:
			currentChoice.choice_hasPicture = False
	currentChoice.save()

def getQuestionaireByID(qid):
	currentQuestionaire = Questionaire.objects.get(questionaire_md5 = qid)
	return_dict = dict()
	type_switcher = {
		"VO" : "vote",
		"LW" : "recruit",
		"SU" : "enroll"
	}
	status_switcher = {
		"SA" : "pending",
		"LA" : "already",
		"IN" : "new",
		"PA" : "pause"
	}
	return_dict["act_type"] = type_switcher[currentQuestionaire.questionaire_type]
	return_dict["act_status"] = status_switcher[currentQuestionaire.questionaire_status]
	return_dict["act_title"] = currentQuestionaire.questionaire_title
	return_dict["act_description"] = currentQuestionaire.questionaire_introduction
	return_dict["qst_num"] = currentQuestionaire.questionaire_numOfQues
	return_dict["time"] = currentQuestionaire.questionaire_time
	questionList = getQuestionsByQuestionaire(qid)
	return_dict["questions"] = questionList
	return return_dict

def getQuestionsByQuestionaire(qid):
	returnList = list()
	currentQuestionList = Question.objects.filter(questionaire_id__questionaire_md5 = qid)
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

	if qst.question_mustfill == True:
		return_dict["qst_must"] = "true"
	else:
		return_dict["qst_must"] = "false"
	if qst.question_type == "FI":
		return_dict["rows"] = qst.question_fillinrow
		return_dict["hint"] = qst.question_fillinhint
		return_dict["check"] = qst.question_fillincheck
	else:
		return_dict["option_num"] = qst.question_choices
		if ((qst.question_type == "MU") or (qst.question_type == "VO") or(qst.question_type == "MA")):
			if qst.question_maxfill != None:
				return_dict["max_selected"] = qst.question_maxfill
			if qst.question_minfill != None:
				return_dict["min_selected"] = qst.question_minfill
		if qst.question_displayVotes == True:
			return_dict["display_vote"] = "true"
		else:
			return_dict["display_vote"] = "false"
		if qst.question_ipTimes != None:
			return_dict["ip_times"] = qst.question_ipTimes
		else:
			return_dict["ip_times"] = ""
		if qst.question_dayTimes != None:
			return_dict["day_times"] = qst.question_dayTimes
		else:
			return_dict["day_times"] = ""
		optionList = list()
		currentChoices = Choice.objects.filter(question = qst)
		for choice in currentChoices:
			optionList.append("###" + choice.choice_text + "###")
		return_dict["option"] = optionList
	return return_dict

def fillQuestionaire(dict):
	currentQuestionaire = Questionaire.objects.get(questionaire_md5 = dict["act_id"])
	currentQuestionaire.questionaire_numOfFilled = currentQuestionaire.questionaire_numOfFilled + 1
	currentQuestionaire.save()
	currentQuestionList = Question.objects.filter(questionaire_id = currentQuestionaire)
	questionCount = currentQuestionaire.questionaire_numOfQues
	currentFiller = Filler(
		filler_ip = dict["IP"],
		filler_address = dict["address"],
		filler_questionaire = currentQuestionaire,
		filler_time = dict["submitTime"]
		)
	currentFiller.save()
	filledList = dict.keys()
	output = open('api.txt', 'w')
	for qst in currentQuestionList:

		output.writelines("qst" + str(qst.id) + "\n")
		if ("qst" + str(qst.id)) in filledList:
			
			output.writelines("qst" + str(qst.id) + "\n")
			output.writelines(str(filledList) + "\n")
			choice = None
			if qst.question_type == "FI":
				text = dict[("qst" + str(qst.id))]
				currentAnswer = Answer(
					answer_filler = currentFiller,
					answer_question = qst,
					answer_content = text,
					answer_choice = choice
					)
				currentAnswer.save()
			else:
				for oneChoice in dict["qst" + str(qst.id)]:
					#print oneChoice
					order = int(oneChoice[6:])
					choice = Choice.objects.get(
						question = qst,
						choice_order = order
						)
					text = choice.choice_text
					currentAnswer = Answer(
						answer_filler = currentFiller,
						answer_question = qst,
						answer_content = text,
						answer_choice = choice
						)
					currentAnswer.save()

def getFillers(act_id):
	currentQuestionaire = Questionaire.objects.get(questionaire_md5 = act_id)
	currentFillerList = Filler.objects.filter(filler_questionaire = currentQuestionaire)
	returnList = list()
	for Fill in currentFillerList:
		returnList.append(makeFillerDict(Fill))
	return returnList

def makeFillerDict(Fill):
	dict = {
		"id" : Fill.id,
		"fillin_time" : Fill.filler_time,
		"ip" : Fill.filler_ip,
		"city" : Fill.filler_address
	}
	return dict

def getQuestionFill(act_id, qst_id, fillin_id):
	currentFiller = Filler.objects.get(id = fillin_id)
	currentQuestion = Question.objects.get(id = qst_id)
	currentAnswer = Answer.objects.filter(answer_filler = currentFiller, answer_question = currentQuestion)
	if len(currentAnswer) == 0:
		return ""
	#print len(currentAnswer)
	if currentQuestion.question_type == "FI":
		cA = Answer.objects.get(answer_filler = currentFiller, answer_question = currentQuestion)
		return cA.answer_content
	if currentQuestion.question_type == "SI":
		cA = Answer.objects.get(answer_filler = currentFiller, answer_question = currentQuestion)
		return cA.answer_choice.choice_order
	if ((currentQuestion.question_type == "MU") or (currentQuestion.question_type == "MA") or (currentQuestion.question_type == "VO")):
		returnList = list()
		#print "?????"
		for answer in currentAnswer:
			#print "???"
			returnList.append(answer.answer_choice.choice_order)
		return returnList

def getStatisticsOfQuestion(qst_id):
	currentQuestion = Question.objects.get(id = qst_id)
	AnswerList = Answer.objects.filter(answer_question = currentQuestion)
	Fillers = Filler.objects.filter(filler_questionaire = currentQuestion.questionaire_id)
	count = len(Fillers)
	returnList = list()
	if currentQuestion.question_type == "FI":
		countDown = 1
		for answer in AnswerList:
			dict = {
				"id" : countDown,
				"content" : answer.answer_content,
				"total" : len(AnswerList)
			}
			returnList.append(dict)
			countDown = countDown + 1
	else:
		Choices = Choice.objects.filter(question = currentQuestion)
		fillerSet = set()
		for answer in AnswerList:
			fillerSet.add(answer.answer_filler)
		total = len(fillerSet)
		returnList = list()
		for oneChoice in Choices:
			answerForOne = AnswerList.filter(answer_choice = oneChoice)
			choiceCount = len(answerForOne)
			if count != 0:
				percentage = int(round(float(choiceCount) / float(count) * 100))
			else:
				percentage = 0
			dict = {
				"id" : oneChoice.choice_order,
				"content" : oneChoice.choice_text,
				"count" : choiceCount,
				"total" : total,
				"percentage" : percentage,
				"max" : "",
				"left" : ""
			}
			if oneChoice.choice_limit != None:
				dict["max"] = str(oneChoice.choice_limit)
				answers = Answer.objects.filter(answer_choice = oneChoice)
				dict["left"] = str(oneChoice.choice_limit - len(answers))
			if oneChoice.choice_hasPicture != None:
				if oneChoice.choice_hasPicture == True:
					dict["has_image"] = "true"
				else:
					dict["has_image"] = "false"
			returnList.append(dict)
	return returnList

