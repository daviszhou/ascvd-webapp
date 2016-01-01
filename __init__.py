import os
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def homepage():

	title = 'Epic Tutorial'
	paragraph = ['While the deployment is happening, you may see a syntax error during the install for gunicorn about invalid syntax for the line yield from self.wsgi.close(). That error can be ignored.', 'While the deployment is happening, you may see a syntax error during the install for gunicorn about invalid syntax for the line yield from self.wsgi.close(). That error can be ignored.']

	return render_template('index.html', title=title, paragraph=paragraph)

@app.route('/about')
def aboutpage():

	title = "About the site"
	paragraph = ["While the deployment is happening, you may see a syntax error during the install for gunicorn about invalid syntax for the line yield from self.wsgi.close(). That error can be ignored.', 'While the deployment is happening, you may see a syntax error during the install for gunicorn about invalid syntax for the line yield from self.wsgi.close()."]

	page_type = 'about'
	return render_template('index.html', title=title, paragraph=paragraph, page_type=page_type)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5020))
	app.run(host='0.0.0.0', port=port)
	app.run(debug=True)