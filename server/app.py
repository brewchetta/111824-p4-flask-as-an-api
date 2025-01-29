#!/usr/bin/env python3

from flask import request, make_response, jsonify
from config import app, db
from models import Puppy

# ROUTES #######################

@app.get('/')
def main_route():
    print("--------------------HELLO------------------")
    return make_response( "<h1>BIG SERVER ERROR 500</h1>", 500 )
    # for whatever reason we're choosing to send back an error and a 500 status code


@app.post('/') # this will only fire for a post request
def main_post():
    return make_response( "<h1>THIS IS A POST REQUEST</h1>", 200 )

# @app.get('/puppies')
# def puppies():
#     return make_response( jsonify({ "name": 'Wilfred', "age": 6 }), 200 )
    # jsonify allows us to transform the dict into json format

# GET ALL
@app.get('/puppies')
def all_puppies():
    all_puppies = Puppy.query.all()
    puppy_dictionaries = [ puppy.to_dict() for puppy in all_puppies ] # list comprehension
    return make_response( jsonify(puppy_dictionaries), 200 )


# GET ONE
@app.get('/puppies/<int:id>')
def get_first_puppy(id):
    first_puppy = Puppy.query.where(Puppy.id == id).first()
    if first_puppy:
        return make_response( jsonify( first_puppy.to_dict() ), 200 )
    else:
        return make_response( jsonify( { "error": "Not found" } ), 404 )

# CREATE
@app.post('/puppies')
def post_brand_new_puppy():
    try:
        body = request.json
        new_pup = Puppy( 
            name=body.get('name'), 
            breed=body.get('breed') 
        )
        db.session.add(new_pup)
        db.session.commit()
        return new_pup.to_dict(), 201
    
    except Exception:
        return make_response( jsonify( { "error": "Something went wrong..." } ), 400 )

# fetch('/puppies', {
#     "method": 'POST',
#     "headers": {},
#     "body": JSON.stringify( {name: "Jim", breed: "Poodle"} )
# })


# UPDATE

# DELETE

# RUN ##########################

if __name__ == '__main__':
    app.run(port=5555, debug=True)