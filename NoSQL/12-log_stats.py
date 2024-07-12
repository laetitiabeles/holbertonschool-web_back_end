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
        count = logs.count_documents({"method": m})
        print(f"\tmethod {m}: {count}")
    filter_path = {"method": "GET", "path": "/status"}
    count_path = logs.count_documents(filter_path)
    print(f"{count_path} status check")
