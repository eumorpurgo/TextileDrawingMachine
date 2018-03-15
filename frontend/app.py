import os
from flask import Flask, jsonify, render_template, request, url_for, session, redirect

IMAGE_FOLDER = 'data/uploads/'

app = Flask(__name__)
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

@app.route('/upload', methods=['POST'])
def uploadFile():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"success":False})
        file = request.files['file']

        if file.filename == '':
            return jsonify({"success":False})
        if file:
            file.save(os.path.join(app.config['IMAGE_FOLDER'], file.filename))
            return jsonify({"success":True})

@app.route('/generate', methods=['GET', 'POST'])
def convertFile():
    if request.method == 'GET':
        filename = request.args.get('fileName')
        filepath = str(IMAGE_FOLDER) + str(filename)
        speed = request.args.get('speed')
        tooldiameter = request.args.get('toolDiameter')
        fillingoption = request.args.get('fillingOption')
        imagesize = request.args.get('imageSize') 
        print("Generating gcode for file: " + filepath)
        print("Speed is: " + str(speed))
        print("Tool diameter is: " + str(tooldiameter))
        print("Filling option is: " + str(fillingoption))
        print("Image size in mm: " + str(imagesize))
        os.system("python3 ../contours/picture2gcode.py" 
            + " --input-path " + str(filepath) 
            + " --fill " + str(fillingoption)
            + " --tool-diameter-in-mm " + str(tooldiameter)
            + " --speed " + str(speed)
            + " --image-width-in-mm "+ str(imagesize)
            + " --hd-smoothing")

    return jsonify({"success":True})

@app.route('/help')
def helpPage():
    return render_template('help.html')

@app.route('/convert')
def convertFormPage():
    return render_template('convert_form.html')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = False)
