from flask import Flask,request,jsonify

app = Flask(__name__)
data = [
    {
        'Id':1,
        'Name':'Arpit',
        'Contact':'9922004282',
        'Done':False
    },
    {
        'Id':2,
        'Name':'Rakesh',
        'Contact':'7659466228',
        'Done':False
    }
]


@app.route('/add-contact',methods=['POST'])
def addContact():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Please Provide Contact Data'
        },400)

    contactData = {
        'Id':data[-1]['Id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact',''),
        'Done':False
    }
    data.append(contactData)
    return jsonify({
        'status':'success',
        'message':'Contact Data Added Successfully'
    })


@app.route('/get-contact')
def getContact():
    return jsonify({
        'data':data
    })

if __name__ =='__main__':
    app.run()