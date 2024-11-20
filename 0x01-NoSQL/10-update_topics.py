#!/usr/bin/env python3
""" This module contains the `update_topics` function """
import pymongo
from typing import List


def update_topics(mongo_collection: pymongo.synchronous.collection.Collection,
                  name: str,
                  topics: List[str]) -> None:
    """ changes all topics of a school document based on the name """
    mongo_collection.update_many({'name': name},
                                {'$set': {'topics': topics}})