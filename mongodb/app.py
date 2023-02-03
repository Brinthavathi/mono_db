from flask import Flask,render_template
import requests
from pymongo import MongoClient

app=Flask(__name__)
client=MongoClient("mongodb://127.0.0.1:27017")
@app.route("/",methods=['post','get'])
def api():
    lis=[145488,146679,147951,147197,147532]
    l=[]
    for i in lis:
        url="https://api.mfapi.in/mf/"+str(i)
        resp=requests.get(url)
        temp=resp.json().get('meta').get('fund_house')
        new_get=resp.json().get('data')[0].get('nav')
        temp1={'fund_house':temp,"nav":new_get}
        l.append(temp1)

    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client.users
    collection=database.fund
    collection.insert_many(l)
    client.close()
    return render_template("index.html",data=l)

@app.route("/update")
def update():
    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client.users
    collection=database.students
    collection.update_many({"author" : "sakthi"},{"$set" : {"subject" : "bad"}})
    client.close()
    return "success"

@app.route("/delete")
def delete():
    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client.users
    collection=database.students
    collection.delete_many({"author" : "siva"})
    client.close()
    return "success"

if __name__=='__main__':
    app.run(debug=True)