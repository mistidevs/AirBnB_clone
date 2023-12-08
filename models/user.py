#!/usr/bin/python3
"""Def The User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """

    def __init__(self, *args, **kwargs):
        """metode of initializing"""
        super().__init__(*args, **kwargs)

    email = ""
    password = ""
    first_name = ""
    last_name = ""
