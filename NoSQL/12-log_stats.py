#!/usr/bin/env python3
""" Log stats """


from pymongo import MongoClient


if __name__ == "__main__":
    """ provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    total = logs.count_documents({})
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{total} logs")
    print("Methods:")
    for m in method:
        count = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    stats = logs.count_documents({"method": "GET", "path": "/status"})

    print(f"{stats} status check")
