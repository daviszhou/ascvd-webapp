import os
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def homepage():

	title = 'Title'
	paragraph = ['Paragraph Text']

	return render_template('index.html', title=title, paragraph=paragraph)

@app.route('/about')
def aboutpage():

	title = "About the site"
	paragraph = ['Paragraph Text']

	page_type = 'about'
	return render_template('index.html', title=title, paragraph=paragraph, page_type=page_type)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5020))
	app.run(host='0.0.0.0', port=port)
	app.run(debug=True)