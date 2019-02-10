from flask import request, jsonify, make_response
from .views import bp_1
from ..models.models import Parties

parties_list = []


@bp_1.route('/parties', methods=['POST'])
def create_party():
    '''Create a party'''
    try:
        data = request.get_json()
        id = len(parties_list) + 1
        name = data['name']
        hq_address = data['hq_address']
        logo_url = data['logo_url']
        chairperson = data['chairperson']


        #Create instance of Parties and pass in data
        new_party = Parties(id, name, hq_address, logo_url, chairperson)
        parties_list.append(new_party)
    
    
        #Loop through the parties list to return the recently added item
        for party in range(len(parties_list)):
            if (parties_list[party]['id']) == int(id):
                return make_response(jsonify({
                "status": 201,
                "message": "Party Created Successfully",
                  "data": [{ "id": parties_list[party]['id'],
                 "name": parties_list[party]['name'],
                  "chairperson": parties_list[party]['chairperson']
                 }]
                   }), 201)     
    except:
        return jsonify({
                "status": 400,
                "message": "Some field(s) are missing"
        }), 400
    
    #Create instance of Parties and pass in data
    new_party = Parties(id, name, hq_address, logo_url, chairperson)
   
    
    

    parties_list.append(new_party)
    
    
    #Loop through the parties list to return the recently added item
    for party in range(len(parties_list)):
        if (parties_list[party]['id']) == int(id):
            return make_response(jsonify({
            "status": 201,
            "message": "Party Created Successfully",
            "data": [{ "id": parties_list[party]['id'],
                 "name": parties_list[party]['name'],
                  "chairperson": parties_list[party]['chairperson']
                 }]
    }), 201)
        



@bp_1.route('/parties', methods=['GET'])
def get_party():
    if len(parties_list) > 0:
        return make_response(jsonify({
            "status": 200,
            "message": "Request was successful",
            "data": [party.__dict__ for party in parties_list]
        }), 200)

    return make_response(jsonify({
        "status": 404,
        "message": "No Parties Available"
    }), 404)

@bp_1.route('/parties/<int:id>', methods=['GET'])
def get_party_byid(id):
    for party in range(len(parties_list)):
        if (parties_list[party]["id"]) == int(id):
            return jsonify({
                "status": 200,
                "message": "Request was successful",
                "data": [{
                   "id": parties_list[party]["id"],
                   "name": parties_list[party]["name"],
                   "hq_address": parties_list[party]["hq_address"]
                }]
                    
            }), 200
        
    return jsonify({
        "status": 404,
        "message": "Resource could not be found",
                   }), 404


@bp_1.route('/parties/<int:id>', methods=['DELETE'])
def delete_party(id):
    for party in range(len(parties_list)):
        if (parties_list[party]["id"]) == int(id):
            parties_list.pop(party)
            return jsonify({
                "status": 200,
                "data": [{
                "message": "Deletion of the party was successful"
                }]
                    
            }), 200

         
    return jsonify({
        "status": 404,
        "message": "Resource could not be found",
    }), 404



@bp_1.route('/parties/<int:id>/<string:name>', methods=['PATCH'])
def edit_party(id, name):
    global parties_list
    for i in range(len(parties_list)):
        if parties_list[i]['id']== id:
            party = parties_list[i]
            party['name'] = name
            parties_list = party
    
            return jsonify({
                "status": 200,
                 "message": "Party name was succesfully updated",   
                "data": [{
                    "id": id,
                    "name" : name
                }]}), 200
        
    return jsonify({
        "status": 404,
        "message": "Resource could not be found",
    }), 404

       
            
        