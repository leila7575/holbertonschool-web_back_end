#!/usr/bin/env python3
""" contains function update_topics."""
from pymongo import MongoClient
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]):
    """Changes all topics of a school document based on the name."""
    query = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_one(query, update)
