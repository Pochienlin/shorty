from flask import Flask, redirect, request, jsonify
from flask_cors import CORS
import json
import requests
import os
from invokes import invoke_http

app = Flask(__name__)
CORS(app)

firebase_url='https://urlshorty-f628f-default-rtdb.asia-southeast1.firebasedatabase.app/'
root_url="localhost:5000/"
app = Flask(__name__)

# route includes get method that retrieves the shortened key
@app.route('/<string:shortID>')
def goto(shortID):
    #------ prepare to retrieve the url path based on the key
    api_endpoint=firebase_url+shortID+".json"
    # print("calling:", api_endpoint)
    #------ Firebase call to retrieve destination url
    result=invoke_http(api_endpoint, method="GET", json=None)
    # print('requested and retrieved: ',result)
    #------ error handle
    if not(result):
        print("\n failed to retrieve the results")
    # if all is successful, the app redirects the user to the destination URL retrieved
    return redirect(result,code=302)


@app.route('/add',methods=["POST"])
def add_new():
    #Use form POST HTTP method to retrieve the destination URL to add
    if request.method=="POST":
        # print("received order: ",request.args.get("new_url"))
        new_url = request.args.get("new_url")
        # print("\nReceived a new order:", new_url)
        #-------retrieve current count from Firebase
        api_endpoint=firebase_url+"count.json"
        count_dict=invoke_http(api_endpoint, method="GET", json=None)
        count=int(count_dict)
        # print("\nCount is: ",count)

        # ------add a new URL into Firebase
        api_endpoint = firebase_url+".json"
        new_entry={str(int(count)+1):new_url}
        result=invoke_http(api_endpoint, method="PATCH", json=new_entry)
        #-------update count
        new_count=str(count+1)
        invoke_http(firebase_url+"count.json", method="PUT", json=new_count)
        # print(count_result)
        #-------return the shortened url to the caller
        for key, value in result.items():
            return root_url+key
    return False 

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)