#!/usr/bin/env python3

from flask import request, make_response, jsonify
from config import app, db
from models import Puppy, Toy

# HELPERS ######################

def find_puppy_by_id(id):
    return Puppy.query.where(Puppy.id == id).first()

# ROUTES #######################

# GET ALL PUPPIES
@app.get('/puppies')
def all_puppies():
    all_puppies = Puppy.query.all()
    puppy_dictionaries = [ puppy.to_dict() for puppy in all_puppies ] # list comprehension
    return puppy_dictionaries, 200


# GET ONE PUPPY
@app.get('/puppies/<int:id>')
def get_puppy(id):
    found_puppy = find_puppy_by_id(id)
    if found_puppy:
        return found_puppy.to_dict(), 200 
    else:
        return { "error": "Not found" }, 404 


# CREATE PUPPY
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
        return { "error": "Something went wrong..." }, 400


# UPDATE PUPPY
@app.patch('/puppies/<int:id>')
def patch_puppy(id):
    found_puppy = find_puppy_by_id(id)
    if found_puppy:
        try:
            body = request.json
            for key in body:
                setattr( found_puppy, key, body[key] )
            db.session.add(found_puppy)
            db.session.commit()
            return found_puppy.to_dict(), 202
        except Exception:
            return { "error": "Something went wrong..." }, 400
    else:
        return { "error": "Not found" }, 404
    

# DELETE PUPPY
@app.delete('/puppies/<int:id>')
def delete_puppy(id):
    found_puppy = find_puppy_by_id(id)
    if found_puppy:
        db.session.delete(found_puppy)
        db.session.commit()
        return {}, 204
    else:
        return { "error": "Not found" }, 404
    

# GET ALL TOYS
@app.get('/toys')
def get_toys():
    all_toys = Toy.query.all()
    toy_dicts = [ toy.to_dict() for toy in all_toys ]
    return toy_dicts, 200


@app.post('/toys')
def post_toy():
    try:
        body = request.json
        new_toy = Toy( 
            name=body.get('name'), 
            puppy_id=body.get('puppy_id') 
        )
        db.session.add(new_toy)
        db.session.commit()
        return new_toy.to_dict(), 201
    except Exception as e:
        return { 'error': str( e ) }, 400



# RUN ##########################

if __name__ == '__main__':
    app.run(port=5555, debug=True)