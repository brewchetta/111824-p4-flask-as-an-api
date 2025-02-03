from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


# MODELS ################

class Pen(db.Model, SerializerMixin):

    __tablename__ = 'pens_table'

    id = db.Column(db.Integer, primary_key=True)

    brand = db.Column(db.String, nullable=False) # the nullable here doesn't do much anymore bc of the validation
    color = db.Column(db.String)
    clickable = db.Column(db.Boolean, default=False)
    length = db.Column(db.Float)
    price = db.Column(db.Float)

    # VALIDATIONS
    @validates('brand') # which attributes are we validating here?
    def validate_brand(self, key, new_value):
        # if this is not good throw an error
        if not isinstance(new_value, str):
            raise ValueError('Pen brand must be a string')
        if len(new_value) < 2:
            raise ValueError('Pen brand must be at least two characters')
        # otherwise return the new_value
        return new_value

    @validates('length', 'price')
    def validate_are_positive(self, key, new_value): # key is either 'price' or 'length'
        if not isinstance(new_value, int) and not isinstance(new_value, float):
            raise ValueError(f"Pen {key} must be an integer or float")
        if new_value <= 0:
            raise ValueError(f'Pen {key} must be a positive value')
        return new_value
    
    @validates('color')
    def validate_color(self, key, new_value):
        colors = ('red', 'blue', 'black', 'orange') # valid pen colors
        if not new_value.lower() in colors:
            raise ValueError('Pen color must be red, blue, black, or orange')
        return new_value.lower() # this will lowercase the value as it goes into the db
    
    @validates('clickable')
    def validate_clickable(self, key, new_value):
        if not isinstance(new_value, bool):
            raise ValueError('Pen clickable must either be True or False')
        return new_value