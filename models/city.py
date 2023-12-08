#!/usr/bin/python3
"""Def City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Public class attributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """initialize methode"""
        super().__init__(*args, **kwargs)

    state_id = ""
    name = ""
