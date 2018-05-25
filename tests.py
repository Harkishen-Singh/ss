import datetime
n ='rec__' +str(datetime.datetime.now())
print(n[:10])
a = n.replace('-','_')
print(a)
from pymongo import MongoClient
url = 'mongodb+srv://harkishen:Bbsr131@cluster0-zmd3i.mongodb.net/test?retryWrites=true'
#url = 'mongodb://127.0.0.1:27017'
dbn = 'test'
client = MongoClient(url)
db = client[dbn]
coll = db['these']
obj = {
	'name':'harkishen singh',
	'branch':'computer science and engineering',
	'college':'college of engineering and technology',
	'place':'bhubaneswar',
	'native':'amritsar, punjab',
	'country':'india'
}
coll.insert_one(obj)
print('Inserted !')