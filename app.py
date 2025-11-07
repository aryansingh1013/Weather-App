from flask import Flask, request, render_template
from main import getWheather

app= Flask(__name__)
@app.route("/",methods=["GET","POST"])

def home():
    Wheather=""
    if request.method=="POST":
        city=request.form["city"]
        Wheather=getWheather(city)
        
    return render_template("index.html",Wheather=Wheather)
    
if __name__=="__main__":
    app.run(debug=True)