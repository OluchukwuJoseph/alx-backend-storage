#!/usr/bin/env python3
""" This script contains the `insert_school` function """
from typing import Dict
import pymongo
import bson


def insert_school(mongo_collection: pymongo.synchronous.collection.Collection,
                  **kwargs: Dict) -> bson.objectid.ObjectId:
    """ inserts a new document in a collection based on kwargs """
    new_document = mongo_collection.insert_one(kwargs)

    return new_document.inserted_id
