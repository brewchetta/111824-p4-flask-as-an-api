#!/usr/bin/env python3

from flask import request, make_response, jsonify
from config import app, db
from models import Pen

# ROUTES #######################

@app.get('/pens')
def all_pens():
    # step one: get all the pens
    all_pens = Pen.query.all()
    # step two: make them into dictionaries
    pen_dicts = [ pen.to_dict() for pen in all_pens ] # list comprehension
    # step three: return it
    return pen_dicts, 200

@app.post('/pens')
def post_pen():
    try: # try to do this
        # step one: get body data
        body = request.json
        # step two: make the pen object
        new_pen = Pen(
            color=body.get('color'),
            clickable=body.get('clickable'),
            length=body.get('length'),
            brand=body.get('brand'),
            price=body.get('price')
        )
        db.session.add(new_pen)
        db.session.commit()
        # step three: return it
        return new_pen.to_dict(), 201
    
    except ValueError as e: # if there is a specific validation error do this
        return { "error": str(e) }, 400

    except Exception as e: # if there is a generic error then do this
        return { "error": str(e), "image": "Some gif url goes here" }, 400


# RUN ##########################

if __name__ == '__main__':
    app.run(port=5555, debug=True)