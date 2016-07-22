# -*- coding: utf-8 -*-

import csv
import json
from tools import *
from models import *
from netacad import celery
import random, time


@celery.task(bind=True)
def parser(self, file2parse):
	f = open('netacad/map.json', 'r')
	keys_map = json.loads(f.read())
	
	with open('netacad/csv-files/'+file2parse, 'rU') as csvfile :
		counter = csv.reader(csvfile,  dialect=csv.excel_tab, delimiter=';')

		line = 1
		nbLine = 0
		reader = []
		keys = {}
		lineStart = 9999
		
		for row in counter:
			nbLine += 1
			reader.append(row)
			
		self.update_state(state='RUNNING', meta={'current': 1, 'total': nbLine})

		for row in reader:
			if line == 2:
				date = getDate(row[0])
				
			if row[0] == "Institution":
				keys = getKeys(row, keys, 1)
				lineStart = line+1
			
			if line == lineStart:
				keys = getKeys(row, keys, 2)
				
			if line > lineStart and row[keys[keys_map["country"]]] == "France":
				institu = Institution()
				
				try:
					academy = Institution.select().where(Institution.num_id_netacad == row[keys[keys_map["institutions"]["id"]]]).get()
					institu.id_institution = academy.id_institution
				except Institution.DoesNotExist:
					pass
				
				for key in keys_map["institutions"]["keys"]:
					setattr(institu, key[0], row[keys[key[1]]].decode('latin-1').encode('utf-8'))
					
				institu.save()
				
				institu = Institution.select().where(Institution.num_id_netacad == row[keys[keys_map["institutions"]["id"]]]).get()
				
				metric = Metrics()
				
				for key in keys_map["metrics"]:
					if row[keys[key[1]]] == "":
						row[keys[key[1]]] = 0
					else:
						row[keys[key[1]]] = row[keys[key[1]]].replace('\xca', '')
						
					setattr(metric, key[0], row[keys[key[1]]])
				
				metric.year_time = date["year"]
				metric.month_time = date["month"]
				metric.day_time = date["day"]
				metric.date_resume = date["resume"]
				metric.id_institution = institu.id_institution
					
				metric.save()
			
			if line%30 == 0:
				self.update_state(state='RUNNING', meta={'current': line, 'total': nbLine})
			line += 1
    
	return {'current': 100, 'total': 100, 'status': 'COMPLETED', 'msg': 'Task completed!'}
