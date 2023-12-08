#!/usr/bin/python3
"The BaseModel class that all classes inherit from"
import copy
from datetime import datetime
import uuid


class BaseModel:
    """The nitty gritties of the BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Function that initialises the values"""
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        """Returning string representation of the class"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        from models import storage
        """Updates the updated_at variable"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        my_dict = copy.deepcopy(self.__dict__)
        my_dict['created_at'] = str(my_dict['created_at'].isoformat())
        my_dict['updated_at'] = str(my_dict['updated_at'].isoformat())
        my_dict['__class__'] = type(self).__name__
        return my_dict
