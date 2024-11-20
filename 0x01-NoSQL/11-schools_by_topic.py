#!/usr/bin/env python3
""" This script contains the `schools_by_topic` function """
from typing import List, Dict

def schools_by_topic(mongo_collection, topic: str) -> List[Dict]:
    """ returns the list of school having a specific topic """
    documents: List[Dict] = []
    print(type(topic))
    for doc in mongo_collection.find({'topics': {'$all': [topic]}}):
        documents.append(doc)

    return documents
