#!/usr/bin/env python3
""" This script provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = collection.count_documents({'method': method})
        print(f'\tmethod {method}: {method_count}')

    print(f"{collection.count_documents({'method': 'GET', 'path': '/status'})}"
          " status check")

    top_ips = collection.aggregate([{'$group':
                                     {'_id': "$ip", 'count': {'$sum': 1}}},
                                    {'$sort': {'count': -1}},
                                    {'$limit': 10}])
    print('IPs:')
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")
