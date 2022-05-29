from urllib import response
import helper
from flask import Flask,request,Response
import json

# Flask Application Name
app=Flask(__name__)

# Home Route to tell what our application is
@app.route('/')
def hello_world():
    return 'Welcome to ToDo App'

# creating a route to add a new item to the list
@app.route('/item/new',methods=['POST','GET'])
def add_item():
    item=request.args.get('item') # we are getting the details related to item
    #item=req_data['item'] # accessing item from json document
    res_data=helper.add_to_list(item) # adding to the list

    if res_data is None:
        response=Response("{'error': 'Item not added -'}"+item, status=400,mimetype='application/json')
        return response
    
    response=Response(json.dumps(res_data),mimetype='application/json')
    return response

# Creating a route to display all the items
@app.route('/items/all')
def get_all_items():
    res_data=helper.get_all_items()
    response=Response(json.dumps(res_data),mimetype='application/json')
    return response

# Create a route to get a particular item
@app.route('/item/status',methods=['GET','POST'])
def get_item():

    item_name=request.args.get('item')
    status=helper.get_item(item_name)

    if status is None:
        response=Response("{'error': 'Item Not Found - '}"+ item_name,status=404,mimetype='application/json')
        return response 

    res_data={'status':status}
    response=Response(json.dumps(res_data),status=200,mimetype='application/json')
    return response

# Create a route to update the status
@app.route('/item/update',methods=['GET'])
def update_status():
    #req_data=request.args.get('item')
    item=request.args.get('item')
    status=request.args.get('status')

    res_data=helper.update_status(item,status)
    if res_data is None:
        response=Response("{'error': 'Error Updating Item - '"+item+","+status+"}",status=400,mimetype='application/json')
        return response
    
    response=Response(json.dumps(res_data),mimetype='application/json')
    return response

# Create a route to delete the item 
@app.route('/item/remove',methods=['GET'])
def delete_item():
    item=request.args.get('item')

    res_Data=helper.delete_item(item)
    if res_Data is None:
        response=Response("{'error': 'Error Deleting Item -'"+item+"}",status=400,mimetype='application/json')
        return response
    
    response=Response(json.dumps(res_Data),mimetype='application/json')
    return response

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)