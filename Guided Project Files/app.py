# By Simhadri Mohana Kushal - 20BCE1952
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) # Initialize the flask App
model = pickle.load(open('model.pkl', 'rb')) # Load the trained model

@app.route('/')
def helloworld():
    return render_template("index.html")

@app.route('/login', methods = ['POST'])
def predict():
    s0 = request.form["stops"]
    airway = request.form["airway"]
    src = request.form["source"]
    des = request.form["destination"]
    jday = request.form["jday"]
    jmonth = request.form["jmonth"]
    depHr = request.form["dep_hour"]
    depMin = request.form["dep_min"]
    arrHr = request.form["arr_hour"]
    arrMin = request.form["arr_min"]
    durHr = request.form["dur_hour"]
    durMin = request.form["dur_min"]

    
    if(airway == "ai"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11=1,0,0,0,0,0,0,0,0,0,0
    if(airway == "ga"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11=0,1,0,0,0,0,0,0,0,0,0
    if(airway == "ig"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11=0,0,1,0,0,0,0,0,0,0,0
    if(airway == "ja"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11=0,0,0,1,0,0,0,0,0,0,0
    if(airway == "jab"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11=0,0,0,0,1,0,0,0,0,0,0
    if(airway == "mc"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11=0,0,0,0,0,1,0,0,0,0,0
    if(airway == "mcpe"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11=0,0,0,0,0,0,1,0,0,0,0
    if(airway == "sj"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11=0,0,0,0,0,0,0,1,0,0,0
    if(airway == "tj"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11=0,0,0,0,0,0,0,0,1,0,0
    if(airway == "v"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11=0,0,0,0,0,0,0,0,0,1,0
    if(airway == "vpe"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11=0,0,0,0,0,0,0,0,0,0,1
    
    s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,0,0,0

    if(src == "Chennai" or des == "Chennai"):
        s12 = 1
    if(src == "Delhi" or des == "Delhi"):
        s13 = 1
    if(src == "Kolkata" or des == "Kolkata"):
        s14 = 1
    if(src == "Mumbai" or des == "Mumbai"):
        s15 = 1
    if(src == "Cochin" or des == "Cochin"):
        s16 = 1
    if(src == "Delhi" or des == "Delhi"):
        s17 = 1
    if(src == "Hyderabad" or des == "Hyderabad"):
        s18 = 1
    if(src == "Kolkata" or des == "Kolkata"):
        s19 = 1
    if(src == "New Delhi" or des == "New Delhi"):
        s20 = 1
    
    t=[[int(s0),int(s1),int(s2),int(s3),int(s4),int(s5),int(s6),int(s7),int(s8),int(s9),int(s10),int(s11),int(s12),int(s13),int(s14),int(s15),int(s16),int(s17),int(s18),int(s19),int(s20),int(jday),int(jmonth),int(depHr),int(depMin),int(arrHr),int(arrMin),int(durHr),int(durMin)]]
    output= model.predict(t)
    print(output)  
    
    return render_template("index.html",y = "Predicted Flight Price: " + str(output[0]))

if __name__ == '__main__' :
    app.run(debug= False)
