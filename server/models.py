from config import db
from sqlalchemy_serializer import SerializerMixin
# from sqlalchemy.ext.associationproxy import association_proxy
# from sqlalchemy.orm import validates


# MODELS ################

class Puppy(db.Model, SerializerMixin):

    __tablename__ = 'puppies_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    breed = db.Column(db.String)

    def is_good_dog(self):
        return "YES"

    # changes the to_dict for each request
    serialize_rules = ("is_good_dog", "-breed")

    # SerializerMixin writes the to_dict for us
    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "breed": self.breed
    #     }