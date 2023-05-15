from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://nanitave:inteligy@cluster0.cn1aiyy.mongodb.net/farmaapp?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db=client["FarmaApp"]
    datos=db["Farmacia"]
    for documento in datos.find():
        print(documento)
except Exception as e:
    print(e)
#json

