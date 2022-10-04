from asyncio import tasks
from flask import Flask, request
from flask import jsonify

app=Flask(__name__)

@app.route("/add-data",methods=["POST"])

def add_task():

    if not request.json:
     return jsonify({
        "status":"error",
        "message":"Please provide the data!"
     },400)

contact = {
   'id': tasks[-1]['id'] + 1,
   'name':request.json['name'],
   'Contact':request.json.get('Contact',""),
   'done':False
}
app.run(debug=True)
