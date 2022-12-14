from flask import Flask,request,jsonify
from pydantic import BaseModel
from key import Keyword_Spotting_Service


app = Flask(__name__)


@app.route('/predict',methods=["GET","POST"])
def index():
    if request.method == "POST":
        
        file = request.files.get('file')
        print(file)
        if file is  None or file.filename == "":
            return jsonify({"error":"no file"})
        try:
             path = file.read()
             kss = Keyword_Spotting_Service()
             keyword1,keyword2= kss.prediction(path)
             prediction = {'prediction': keyword1}
             return jsonify(prediction)
        except Exception as e:
            return jsonify({"error":str(e)})
    return "OK"



if __name__ == "__main__":
    app.run(debug=True)