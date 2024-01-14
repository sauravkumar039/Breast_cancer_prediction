from flask import Flask, render_template,request
import ml as m

app=Flask(__name__)

global preu
@app.route('/',methods=['POST','GET'])
def fetch():
    if request.method=="POST":
        rw=float(request.form.get("rworst"))
        tw=float(request.form.get("tworst"))
        pw=float(request.form.get("pworst"))
        aw=float(request.form.get("aworst"))
        sw=float(request.form.get("sworst"))
        cw=float(request.form.get("cworst"))
        cow=float(request.form.get("coworst"))
        copw=float(request.form.get("copworst"))
        syw=float(request.form.get("syworst"))
        fdw=float(request.form.get("fdworst"))
        mainsize=[rw,tw,pw,aw,sw,cw,cow,copw,syw,fdw]
        predisease=m.predict_disease(mainsize)
        if predisease==[1]:
           return render_template("index2.html")
        elif predisease==[0]:
           return render_template("index3.html")
    return render_template("index.html")

   
   
   
if __name__=="__main__":
   app.run(debug=True)