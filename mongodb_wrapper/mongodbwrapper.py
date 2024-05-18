from pymongo import MongoClient
from multipledispatch import dispatch


class MongoDBWrapper:
    mongo_client: MongoClient

    def __init__(self):
        self.mongo_client = None

    def connect(self, address: str) -> bool:
        if self.mongo_client is None:
            self.mongo_client = MongoClient(address)
            return True
        else:
            raise RuntimeError("Connection is already established!")

    @dispatch()
    def list(self):
        if self.mongo_client is None:
            raise RuntimeError("Connection is not established!")
        return self.mongo_client.list_database_names()

    @dispatch(str)
    def list(self, db: str):
        if self.mongo_client is None:
            raise RuntimeError("Connection is not established!")
        return self.mongo_client[db].list_collection_names()
    
    @dispatch(str, str)
    def list(self, db: str, col: str):
        if self.mongo_client is None:
            raise RuntimeError("Connection is not established!")
        return self.mongo_client[db][col].find()

    @dispatch(str, str, dict)
    def list(self, db: str, col: str, filters):
        if self.mongo_client is None:
            raise RuntimeError("Connection is not established!")
        return self.mongo_client[db][col].find(filter=filters)

    def update(self, db: str, col: str, filter, doc):
        if self.mongo_client is None:
            raise RuntimeError("Connection is not established!")
        return self.mongo_client[db][col].update_many(filter, {'$set': doc})

    def insert(self, db: str, col: str, doc):
        if self.mongo_client is None:
            raise RuntimeError("Connection is not established!")
        return self.mongo_client[db][col].insert_many(doc)

    def remove(self, db: str, col: str, filter):
        if self.mongo_client is None:
            raise RuntimeError("Connection is not established!")
        return self.mongo_client[db][col].delete_many(filter)
