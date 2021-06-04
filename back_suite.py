#! flask/bin/python

from flask import Flask, jsonify, abort
import resources.py


app = Flask(__name__)

vendors = [Vendor(1,'sepis cookies', 'sepidj')] # because no DB! 


@app.route('/')
def index():
    return "Welcome to IAM Farmers Market!"

@app.route('/iam_farmer/api/v1.0/vendors', methods=['GET','POST','PUT'])
def get_vendors():
    return jsonify({'vendors': vendors})


def create_vendor():
    if not request.json or not 'name' in request.json:
        abort(400)
    vendor_id = len(vendors)+1 
    vendor = Vendor(vendor_id,request.json['name'],request.json['username'])
    vendors.append(vendor)

    return vendor,201



if __name__ == '__main__':
    app.run(debug=True)



