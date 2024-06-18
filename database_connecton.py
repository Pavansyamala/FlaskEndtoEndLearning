import pymongo 
from urllib.parse import quote_plus

class connection :

    def __init__(self):
        name = quote_plus("pavankasa")
        password = quote_plus("9347649447")
        uri = f"mongodb+srv://{name}:{password}@cluster0.hvbqd7o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.connection = pymongo.MongoClient(uri)

        self.db = self.connection['UsersDatabaseForms']

        self.coll = self.db['UsersInformation'] 


# if __name__ == '__main__':
#     obj = connection()
#     print(obj.connection)
#     data = {"a":1234}
#     obj.coll.insert_one(data)

