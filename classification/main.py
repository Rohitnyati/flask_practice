from flask import Flask,render_template,request
import pymongo
import pickle


object_model=pickle.load(open("lr_student.pkl","rb"))

client=pymongo.MongoClient()

mydb=client["mydb"]

mycol=mydb["people"]

# data={'name':'Rohit','Age':20}
# mycol.insert_one(data)

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

# @app.route('/rohit')
# def rohit():
#<form action ="http://127.0.0.1:5000/success" method="post">

@app.route('/success', methods=["POST"])
def success():
    cgpa1=float(request.form.get('cgpa'))
    iq_1=int(request.form.get('iq'))
    profile_score_1=int(request.form.get('score'))
    result=object_model.predict([[cgpa1,iq_1,profile_score_1]])

    # if result[0]==0:
    #     place="*******************Sorry Not Placed*********************"
    # else:
    #     place="******************Congractulations: placed successfully************************"
    # print(place)
    mycol.insert_one({"CGPA":cgpa1,"IQ":iq_1,"Profile Score":profile_score_1})
    return render_template('success.html',prediction=result)


@app.route('/marks',methods=["POST"])
def mark(score):
    return render_template('mark.html',score=score)


app.run(debug=True)
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     app.run(debug=True,host="0.0.0.0")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
