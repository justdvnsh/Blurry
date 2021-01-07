import os
from flask import render_template, request, redirect, url_for, abort, send_from_directory
from werkzeug.utils import secure_filename
from core import image_validator
from app import app

## Home Page
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        files = os.listdir(app.config['UPLOAD_PATH'])
        return render_template('index.html', title="HOME", files=files)
    
    if request.method == "POST":
        for uploaded_file in request.files.getlist('file'):
            filename = secure_filename(uploaded_file.filename)
            if filename != "":
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config['UPLOAD_EXTENSIONS'] or file_ext != image_validator.validate_image(uploaded_file.stream):
                    abort(400)
                else:
                    uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        return redirect(url_for('index'))
    
@app.route("/uploads/<filename>")
def upload(filename):
    print(os.getcwd())
    print(app.config['UPLOAD_PATH'] + "/" + filename)
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_PATH']), filename)

## About Page
@app.route('/about')
def about():
    return render_template('about.html')

## Pricing Page
@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

## Features Page
@app.route('/features')
def features():
    return render_template('features.html')

## Feedback Form
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

