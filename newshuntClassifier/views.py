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
	
	if len(subjects)>0:
		mostProbableSubject = max(set(subjects), key=subjects.count)
	else:
		mostProbableSubject = "EMPTY"

	response = {}
	response["isNews"] = "yes"
	response["topic"] = mostProbableSubject
	response["label"] = label
	
	return HttpResponse(json.dumps(response), content_type="application/json")