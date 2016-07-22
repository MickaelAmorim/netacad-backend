# -*- coding: utf-8 -*-

import pymysql
import csv
import sys
import re
from functools import wraps
from flask import request,current_app
from flask.ext.jsonpify import jsonify
import json
from openpyxl import load_workbook

# GLOBAL VARIABLES
HOST_DATABASE='10.60.21.3'
USER_DATABASE='netacad'
PASSWD_DATABASE="cisco"
NAME_DATABASE="netacad"


months = dict([("January", "01"), ("February", "02"), ("March", "03"), ("April", "04"), ("May", "05"), ("June", "06"), ("July", "07"), ("August", "08"), ("September", "09"), ("October", "10"), ("November", "11"), ("December", "12")])
    
def support_jsonp(url):
	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			callback = request.args.get(url, False)
			if callback:
				content = str(callback) + '(' + str(f().data) + ')'
				return current_app.response_class(content, mimetype='application/json')
			else:
				return f(*args, **kwargs)
			return takes_a_function(*args, **kwargs)
		return decorated_function
	return decorator

def ConnectToSqlServer():

    if (USER_DATABASE != None and PASSWD_DATABASE != None and HOST_DATABASE != None and NAME_DATABASE != None) :
        try :
            cnx = pymysql.connect(host=HOST_DATABASE, user=USER_DATABASE, passwd=PASSWD_DATABASE, db=NAME_DATABASE, port=3306, autocommit=True)
            cur = cnx.cursor()
        except Exception as e :
            print e
            print '-'*60
            print "ERROR CONNECTION TO DATABASE"
    return cnx, cur

def CloseToSqlServer(cnx, cur):

    try :
        cur.close()
        cnx.close()
    except Exception :
        print Exception
        print '-'*60
        print 'ERROR CLOSE CONNECTION TO DATABASE'
    return 0
    
def getDate(date_document):
	date_document = date_document.replace(',', '')
	date_document = date_document.split(' ')
	month_document = date_document[1]
	year_document = date_document[3]
	day_document = date_document[2]

	if months[month_document] != None :
		date_resume=year_document+"-"+months[month_document]+"-"+day_document
	else:
		date_resume=year_document+"-"+month_document+"-"+day_document
	return {
		"month": month_document,
		"year": year_document,
		"day": day_document,
		"resume": date_resume
	}

def getKeys(row, keys, step):
	if step == 1:
		colnum = 0
		lastCol = ""
		for col in row:
			if col != "":
				lastCol = col.replace("\n", " ")
			keys[colnum] = lastCol
			colnum += 1
		return keys
	elif step == 2:
		colnum = 0
		lastCol = ""
		for col in row:
			keys[colnum] = keys[colnum]+"-"+col.replace("\n", " ")
			colnum += 1
			
		keys = dict((v, k) for k, v in keys.iteritems())
		return keys
