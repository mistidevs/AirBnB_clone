#!/usr/bin/python3
"""Def State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """classes that inherit from BaseModel"""
    def __init__(self, *args, **kwargs):
        """initialize methode"""
        super().__init__(*args, **kwargs)

    name = ""
