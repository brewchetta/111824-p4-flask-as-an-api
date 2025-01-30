from config import db
from sqlalchemy_serializer import SerializerMixin
# from sqlalchemy.ext.associationproxy import association_proxy


# MODELS ################

class Puppy(db.Model, SerializerMixin):

    __tablename__ = 'puppies_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    breed = db.Column(db.String)

    toys = db.relationship('Toy', back_populates='puppy')

    serialize_rules = ('-toys.puppy',)

class Toy(db.Model, SerializerMixin):

    __tablename__ = 'toys_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies_table.id'))

    puppy = db.relationship('Puppy', back_populates='toys')

    serialize_rules = ('-puppy.toys', '-puppy.breed')