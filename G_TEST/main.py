from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def meter():
	data = requests.get('https://snapmeter.com/api/v2/531e19848df5cb0b35014e85/meters/2166484536790/bill-summary?token=6d547442-417b-41a3-8838-b022f9c2974d').json()
	print (data['data'])
	return render_template('index.html', data=data['data'])