import os
from flask import Flask, render_template, flash, request, redirect, url_for #import flask etc
from werkzeug.utils import secure_filename
import analysis

UPLOAD_FOLDER = r'C:\Users\milly\snapapp\uploads'
ALLOWED_EXTENSIONS = {'json'}

app = Flask(__name__) #create new instance of app

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # PATH TO UPLOAD FOLDER
app.config['MAX_CONTENT_PATH'] = 16*1024*1024 #max size in bites of upload

def allows_files(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/') #map route / to function home
def home():
    return render_template('home.html')

@app.route('/upload', methods=["GET","POST"])
def upload():
    return render_template("upload_file.html")

@app.route('/uploader', methods = ['GET','POST'])
def upload_file():
    if request.method == "POST": #verify request method is POST
        f = request.files['file1']
        filename = secure_filename(f.filename)
        file_ = f.read()
        graph = request.form['graph']
        if graph == "svr":
            analysis.analyse_snap_data_3(file_)
        else:
            analysis.analyse_snap_data_4(file_)
        flash('File successfully uploaded')
        return redirect('/upload')
                                    
@app.route('/how-to')
def how_to():
    return render_template("how-to.html")

if __name__== '__main__':
    app.run(debug=True) #run on local server, debugging