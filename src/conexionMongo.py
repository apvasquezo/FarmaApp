from pymongo import MongoClient
Mongo_url='mongodb://localhost'
farma=MongoClient(Mongo_url)
#base de datos
db=farma['FarmaApp']
#coleccion
datos= db['consultas']

#json
datos.insert_one({"producto": "Dolex 500", "Precio":1500, "ubica":"Farmatodo","fecha":"2023/04/05"})
