#!/usr/bin/env python3
""" This script contains the `list_all` function """
import pymongo
from typing import List, Dict


def list_all(
        mongo_collection: pymongo.synchronous.collection.Collection
        ) -> List[Dict]:
    """ Returns a list of all documents in a collection """
    documents: List[Dict] = []
    for document in mongo_collection.find():
        documents.append(document)

    return documents
