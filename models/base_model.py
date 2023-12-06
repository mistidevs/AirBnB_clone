#!/usr/bin/python3
"The BaseModel class that all classes inherit from"
from datetime import datetime
import uuid

class BaseModel:
    " The nitty gritties of the BaseModel class"
    def __init__(self, *args, **kwargs):
        "Function that initialises the values"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        "Returning string representation of the class"
        return f"{type(self).__name__} ({self.id}) {self.__dict__}"

    def save(self):
        "Updates the public instance attribute updated_at with the current datetime"
        self.updated_at = datetime.now()

    def to_dict(self):
        "Returns a dictionary containing all keys/values of __dict__ of the instance"
        my_dict = self.__dict__.copy()
        "my_dict = copy.deepcopy(self.__dict__)"
        my_dict['created_at'] = str(my_dict['created_at'].isoformat())
        my_dict['updated_at'] = str(my_dict['updated_at'].isoformat())
        my_dict['__class__'] = type(self).__name__
        return my_dict
        
        
