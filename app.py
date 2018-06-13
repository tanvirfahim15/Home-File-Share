
from flask import Flask, render_template, request, send_file, redirect
from werkzeug import secure_filename
import os

UPLOAD_FOLDER = '/files'

app = Flask(__name__,static_url_path='/files')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
print(os.getcwd())
@app.route('/')
def home():
   return render_template('home.html')

@app.route('/remove')
def remove():
	os.system('rm -f files/*')
	return redirect('/files')

@app.route('/remove/<string:fname>')
def removefile(fname):
	os.system('rm -f files/'+fname)
	return redirect('/files')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		target = os.path.join(APP_ROOT, 'files/')
		print(target)
		if not os.path.isdir(target):
			os.mkdir(target)
		f = request.files['file']
		f.save("/".join([target,f.filename]))
		return redirect('/files')

@app.route('/files/<string:fname>')
def file(fname):
	return send_file('files/'+fname,attachment_filename=fname)

@app.route('/files')
def files():
	data='<a href=\'/\'>Upload</a>-----<a href=\'/remove\'>Remove all</a>'
	for item in os.listdir('files'):
		data=data+'<h1><a href=\'./files/'+item+'\'>'+item+'</a>-----------<a href=\'remove/'+item+'\'>Delete</a></h1>'
	return data

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(host='192.168.1.108', port=80, debug=False)
