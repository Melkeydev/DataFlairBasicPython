from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
import pytube

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/converter', methods=['GET','POST'])
@cross_origin()
def URL_converter():
    if request.method == "POST":



        try:
            url = request.json
            print(url)
            youtube = pytube.YouTube(url)
            video = youtube.streams.first()
            video.download("../../Video",video.title)
            return url 

        except Exception as e:
            print(e)
    elif request.method == "GET":

        return send_file("../../Video/download.jpeg",attachment_filename="Test",as_attachment=True)



@app.route('/getFile')
@cross_origin()
def return_file():
    try:
        return send_file("../../Video/download.jpeg",attachment_filename="Test",as_attachment=True)

    except Exception as e:
        print(e)