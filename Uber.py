#!/usr/bin/python
import requests
import json
import csv
import datetime
import os
from flask import Flask
from flask import request

def init():
	init()
    #init method

app = Flask(__name__)

@app.route("/", methods = ['POST'])

def hello():
	if request.method == 'POST':
		url = "https://www.uber.com/api/fare-estimate"
		params = {"pickupRef":"EjVSYWppdiBDaG93aywgQ29ubmF1Z2h0IFBsYWNlLCBOZXcgRGVsaGksIERlbGhpLCBJbmRpYQ","pickupLat":"28.6328799","pickupLng":"77.21843559999999","destinationRef":"ChIJ46HR1YUbDTkRZivAqP3d4h0"}
		response = requests.request("GET", url=url, params=params)
		response_parsed = json.loads(response.text)["prices"]

		with open('test.csv', 'a') as f:
		    dict_writer = csv.DictWriter(f,fieldnames=['timeStamp','between','fareString','vehicleViewDisplayName','base','fareType','isDistanceUnitMetric','cancellation','minimum','perMinute','safeRideFee','perDistanceUnit'],delimiter=',')
		    dict_writer.writeheader()
		    count = 0
		    for price in response_parsed:
		    	if count <= 1:
		    		time = datetime.datetime.now()
		    		fareString = price["fareString"].encode("utf-8")
		    		vehicleViewDisplayName = price["vehicleViewDisplayName"].encode("utf-8")
		    		base = price["fare"]["base"].encode("utf-8")
		    		fareType = price["fare"]["fareType"].encode("utf-8")
		    		isDistanceUnitMetric = price["fare"]["isDistanceUnitMetric"]
		    		cancellation = price["fare"]["cancellation"].encode("utf-8")
		    		minimum = price["fare"]["minimum"].encode("utf-8")
		    		perMinute = price["fare"]["perMinute"].encode("utf-8")
		    		safeRideFee = price["fare"]["safeRideFee"]
		    		perDistanceUnit = price["fare"]["perDistanceUnit"].encode("utf-8")
		    		count +=1
		    		dict_writer.writerow({'timeStamp':time,'between':"Rajiv Chowk - Indira Gandhi International Airpot",'fareString':fareString,'vehicleViewDisplayName':vehicleViewDisplayName,'base':base,'fareType':fareType,'isDistanceUnitMetric':isDistanceUnitMetric,'cancellation':cancellation,'minimum':minimum,'perMinute':perMinute,'safeRideFee':safeRideFee,'perDistanceUnit':perDistanceUnit})
		   
		f.close()
		return "OK"

if __name__ == __name__:
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)