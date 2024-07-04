import pickle
from flask import Flask,render_template,request
app=Flask(__name__)
load=pickle.load(open('Kidneydisease.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=["GET","POST"])
def predict():
    if request.method=="POST":
        age=int(request.form["age"])
        bp=int(request.form["bp"])
        sg=int(request.form["sg"])
        al=int(request.form["al"])
        su=int(request.form["su"])
        rbc=request.form["rbc"]
        ba=int(request.form["ba"])
        bgr=int(request.form["bgr"])
        bu=int(request.form["bu"])
        sc=int(request.form["sc"])
        sod=request.form["sod"]
        hemo=int(request.form["hemo"])
        pcv=int(request.form["pcv"])
        wc=int(request.form["wc"])
        rc=int(request.form["rc"])
        cad=int(request.form["cad"])
        appet=int(request.form["appet"])
        pe=int(request.form["pe"])
        ane=int(request.form["ane"])
        prediction=load.predict([[age,bp,sg,al,su,rbc,ba,bgr,bu,sc,sod,hemo,pcv,wc,rc,cad,appet,pe,ane]])
        
        if prediction==1:
            result='you have kidney disease'
        else:
            result='you are healthy' 
        return render_template('index.html',prediction_text="{}".format(result))
    return render_template('index.html') 

if __name__=='__main__': 
    app.run(debug=True)
