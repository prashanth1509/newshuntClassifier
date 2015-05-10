from django.http import HttpResponse
from newshuntClassifier.extract import Classifyar
import json

def index(request):
	texts = request.REQUEST['texts']
	label = request.REQUEST['label']

	texts = json.loads(texts)

	cl = Classifyar("https://api.myjson.com/bins/1s1xp")
	cl = cl.getClassifier()

	subjects = []
	for line in texts:
		subjects.append(cl.classify(line))
	
	mostProbableSubject = max(set(subjects), key=subjects.count)

	response = {}
	response["isNews"] = "yes"
	response["topic"] = mostProbableSubject
	response["label"] = label
	
	return HttpResponse(json.dumps(response))