#!/usr/bin/env python3
""" contains function insert_school."""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """Inserts new document in collection."""
    _id = mongo_collection.insert_one(kwargs)
    return _id.inserted_id
