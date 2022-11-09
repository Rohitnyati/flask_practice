from flask import Flask,render_template,request
import pymongo
import pickle

object_model=pickle.load(open("lr_autos.pkl","rb"))


app=Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/success',methods=["POST"])
def result():
    Length=float(request.form.get('length'))
    Width=float(request.form.get('width'))
    NOC=int(request.form.get('noc'))
    Engine=int(request.form.get('engine_size'))
    Bore=float(request.form.get('bore'))
    Horse_power=float(request.form.get('horse_power'))
    result=object_model.predict([[Length,Width,NOC,Engine,Bore,Horse_power]])
    dict={"length":Length,'width':Width,'NOC':NOC,'Engine':Engine,'Bore':Bore,'Horse power':Horse_power,'Price':result}
    #return result
    return render_template('success.html',prediction=dict)


if __name__ == '__main__':
    app.run()