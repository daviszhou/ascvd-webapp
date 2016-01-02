import os
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def homepage():
	viewer = 'clinician'
	description = 'This is the clinician version.'

	return render_template('index.html', viewer=viewer, description=description)

@app.route('/patient')
def patientpage():

	viewer = 'patient'
	description = 'This is the patient version.'

	return render_template('index.html', viewer=viewer, description=description)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5010))
	app.run(host='0.0.0.0', port=port)
	app.run(debug=True)