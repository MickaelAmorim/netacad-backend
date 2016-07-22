# -*- coding: utf-8 -*-

from netacad import app
from tools import *
import urllib
import subprocess
from csvParser import *
import hashlib

@app.route("/.api/netacad/csv/parse/<filename>",  methods=['GET'])
@support_jsonp('get_parse_result')
def runParse(filename):
	newName = hashlib.md5(filename).hexdigest()+".csv"
	urllib.urlretrieve("http://10.228.40.42/netacad-web/upload/uploads/"+filename, "netacad/csv-files/"+newName)
	task = parser.delay(newName)
	return jsonify(summary=json.dumps({"jobID": task.id}))
	
@app.route("/.api/netacad/csv/<taskID>/state",  methods=['GET'])
@support_jsonp('get_parse_state')
def parseState(taskID):
    task = parser.AsyncResult(taskID)
    if task.state == 'PENDING':
        response = {
            'pourcent': 0,
            'msg': 'Pending ...',
            'success': -2
        }
    elif task.state == 'FAILURE':
		response = {
            'pourcent': 100,
            'msg': 'Processing error',
            'success': 0
        }
    elif task.state == 'RUNNING':
		pourcent = (task.info.get('current', 0)*100)/task.info.get('total', 1)
		response = {
            'pourcent': pourcent,
            'msg': 'Processing ...',
            'success': -1
        }
    else:
        response = {
            'pourcent': 100,
            'msg': 'Success!',
            'success': 1
        }
    return jsonify(summary=json.dumps(response))
