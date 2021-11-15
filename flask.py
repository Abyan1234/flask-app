from flask import Flask,jsonify,request

app=Flask(__name__)

tasks=[
    {
        "data":[
            {
                "Contact":"9987644456",
                "Name": "Raiju",
                "done":False,
                "id":1
                
        },
        {
                "Contact":"9876543222",
                "Name": "Rahul",
                "done":False,
                "id":2
        }
        ]
       
    }
]


app.route("/add-data", methods=["POST"])

def add_task():

    if not request.json:

        return jsonify({

            "status":"error",

            "message":"Pleas provide the data"
        },400)


@app.route("/")
def hello_world():
    return "hello world"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },400)

    contact ={

        'id': tasks[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact':request.json.get('Contact', ""),
        'done':False
}
    tasks.append(contact)
    return jsonify({
        "status":"success",
        "message":"Task added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if (__name__=="__name__"):
    app.rundebug=True






