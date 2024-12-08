from mongoengine import Document, StringField, ListField

class Temple(Document):
    name = StringField(required=True)
    location = StringField(default="Unknown")
    built_date = StringField(default="Unknown")
    description = StringField(default="No description available")
    images = ListField(StringField(), default=[])

    meta = {
        'indexes': [
            {'fields': ['$name', '$description'], 'default_language': 'english', 'weights': {'name': 10, 'description': 2}}
        ]
    }

    def to_json(self):
        return {
            "name": self.name,
            "location": self.location,
            "built_date": self.built_date,
            "description": self.description,
            "images": self.images
        }
