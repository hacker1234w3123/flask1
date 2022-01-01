from flask import Flask,jsonify,request

app = Flask(__name__)


Contact = [
{'Contact':9987644456,'name':"Raju" ,'done': False,'id':1},
{'Contact':9876543222,'name':"Rahul" ,'done': False,'id':2}
]

# Get method
@app.route("/")
def getContact():
    return jsonify({'data':Contact})


#Post method
@app.route("/add_Contact",methods = ["POST"])
def add():
    if not request.json:
        return jsonify({"status":"error",'message':'Please provide the data!'})
    else:
        
        task = {'id':Contact[-1]['id']+1 , 
        'name':request.json['name'] , 
        'contact':request.json.get('contact',''),
        'done':False
        }
        Contact.append(task)
        return jsonify({"status":"successfully","message":"the contact list added","contact":Contact})

    


# Run Function
if __name__ == '__main__':
    app.run(debug = True)
