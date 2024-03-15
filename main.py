# Import Libraries below
from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import cv2
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def uploadForm():
    return render_template('upload.html')

@app.route('/', methods = ['POST'])
def uploadVideo():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static/', filename))

    return render_template('upload.html', filename = filename)

@app.route('/display/<filename>')
def display_video(filename):
    return redirect(url_for("static", filename = filename))

if __name__ == '__main__':
    app.run(debug=True)



 







# Define flask 


# Define upload_form() and route the webapp 






# Define upload_video() to get video in defined folder and route the webapp  








# Define display_video() to Display video in defined folder and route the webapp  





if __name__ == "__main__":
    app.run(debug=True)
