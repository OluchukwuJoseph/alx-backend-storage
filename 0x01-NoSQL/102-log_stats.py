#!/usr/bin/env python3
""" This script provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {collection.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {collection.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {collection.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {collection.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE:"
          f" {collection.count_documents({'method': 'DELETE'})}")
    print(f"{collection.count_documents({'method': 'GET', 'path': '/status'})}"
          " status check")

    top_ips = collection.aggregate([{'$group':
                                     {'_id': "$ip", 'count': {'$sum': 1}}},
                                    {'$sort': {'count': -1}},
                                    {'$limit': 10}])
    print('IPs:')
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")
