from flask import Flask, render_template,request
import requests

app = Flask(__name__)
#list1= [149366, 149368, 149365, 149367]
list = []



'''@app.route("/")
def home():
    url = "https://api.mfapi.in/mf/120185"
    resp = requests.get(url)
    return render_template("index.html", data = resp.json().get('data')[0].get('nav'))'''


@app.route("/update", methods=["POST", "GET"])
def fun():
    i = ""
    if request.form.get("input")!=None:
        temp = request.form.get("input")
        url = "https://api.mfapi.in/mf/"+i
        resp = request.get(url)
        temp = resp.json()
        code = temp.get("meta").get("scheme_code")
        house = temp.get("meta").get("fund_house")
        nav = temp.get("data")[0].get("nav")
        dict = {"scheme_code":code, "fund_house":house, "nav":nav}
        i.append(dict)

    return render_template("index.html", data = i)




@app.route("/api", methods=["POST", "GET"])
def fun1():
    i=request.json.get("input")
    url="https://api.mfapi.in/mf/"+str(i)
    resp=request.get(url)
    temp=resp.json()
    code=temp.get("meta").get("scheme_code")
    house=temp.get("meta").get("fund_house")
    nav=temp.get("data")[0].get("nav")
    dict={"scheme_code":code, "fund_house":house, "nav":nav}
    i.append(dict)
    return i


    
    




'''@app.route("/", methods=["POST", "GET"])
def home():
    for i in range(0, len(list1)):
        url = "https://api.mfapi.in/mf/"+str(list1[i])
        resp = requests.get(url)
        fund_house = resp.json().get("meta").get("fund_house")
        nav = resp.json().get("data")[0].get("nav")
        temp = {"id":list1[i], "fund_house":fund_house, "nav":nav}
        list.append(temp)
    var = list
    return render_template("index.html", data = var)'''



    
    



if __name__ == "__main__":
    app.run(debug=True)