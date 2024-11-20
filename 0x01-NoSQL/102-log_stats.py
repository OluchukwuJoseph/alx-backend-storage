#!/usr/bin/env python3
""" This script provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    n_logs = collection.count_documents({})
    print(f'{n_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f'\tmethod {method}: {method_count}')

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')

    top_ips = collection.aggregate([{'$group':
                                     {'_id': "$ip", 'count': {'$sum': 1}}},
                                    {'$sort': {'count': -1}},
                                    {'$limit': 10}])
    print('IPs:')
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")
