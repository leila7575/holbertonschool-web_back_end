#!/usr/bin/env python3
""" contains function list_all."""
from pymongo import MongoClient


def list_all(mongo_collection):
    """Lists all documents in a collection."""
    return list(mongo_collection.find())
