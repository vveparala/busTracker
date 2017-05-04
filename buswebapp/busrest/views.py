# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from busrest.models import Record
# Create your views here.
import logging
import json
import sys

logger = logging.getLogger('django')

@csrf_exempt
def index(request):
	if request.method =="GET":
		return HttpResponse("USE Post method to submit data")
	if request.method == "POST":
		#logger.error(request.body)
		try:
			rec_record=json.loads(request.body)
			#logger.error(rec_record)
			newRecord=Record(user=rec_record['user'],json_str=rec_record['record'])
			newRecord.save()
		except:
			logger.error(sys.exc_info())
			return HttpResponse("Error in Json serialization or missing required fields",status=500)
		return HttpResponse(request.body)
