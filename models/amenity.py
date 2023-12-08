#!/usr/bin/python3
"""Def the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Public class attributes:
    name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """initialize methode"""
        super().__init__(*args, **kwargs)

    name = ""
