from config import db
# from sqlalchemy.ext.associationproxy import association_proxy
# from sqlalchemy_serializer import SerializerMixin
# from sqlalchemy.orm import validates


# MODELS ################

class Puppy(db.Model):

    __tablename__ = 'puppies_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    breed = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "breed": self.breed
        }