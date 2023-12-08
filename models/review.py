#!/usr/bin/python3
"""Def the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Public class attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """initialize methode"""
        super().__init__(*args, **kwargs)

    place_id = ""
    user_id = ""
    text = ""
