from main_part import Core_Base
from pymongo import MongoClient
import datetime
time = datetime.datetime.now()
objArr = []

url = 'mongodb+srv://harkishen:Bbsr131@cluster0-zmd3i.mongodb.net/Weather_record_tests?retryWrites=true'
client = MongoClient(url)
DBname = 'Weather_record_tests'
db = client[DBname]
previous_collections = []
collName = 'rec__'+ str(time)[:10]
collName = collName.replace('-','_')
coll = db[collName]


class Links_to_Database(Core_Base):

    def __init__(self):
        pass
        

    def object_creation_apending(self):
        object = {
            "place" : self.place,
            "state" : self.stateSp,
            "date" : str(time)[:10],
            "time_now" : str(time)[11:],
            "temperature_that_moment" : self.temperature,
            "max_temperature" : self.max_temp,
            "min_temperature" : self.min_temp,
            "avg_temperature" : self.avg_temp,
            "max_probability_rainfall" : self.max_rain_probability,
            "min_probability_rainfall" : self.min_rain_probability,
            "avg_rainfall" : self.avg_rain,
            "humidity": self.humidity,
            "feels_like_that_moment" : self.feel,
            "dew_point" : self.dew_point,
            "visibility" : self.visibility,
            "hourly_forecast" : self.var,
            "rain_array_starting_from_time_now" : self.rains,
            "temp_array_starting_from_time_now" : self.temps,
        }
        objArr.append(object)


cityObject = ['Angul',
'Boudh',
'balangir',
'Bargarh',
'Balasore',
'Bhadrak',
'Cuttack',
'Debagarh',
'Dhenkanal',
'Ganjam',
'Gajapati',
'Jharsuguda',
'Jaipur',
'Jagatsinghpur',
'Khordha',
'Kendujhar',
'Kalahandi',
'Kandhamala',
'koraput',
'Kendrapara',
'Malkanagir',
'Mayurbhanj',
'Nabarangpur',
'Nuapada',
'Nayagarh',
'Puri',
'Rayagada',
'Sambalpur',
'Subarnapur',
'Sundergarh',
'Bhubaneswar',
'Jatni',
'Chilika',
]
state = ['Odisha']

def checks():

        previous_collections = db.collection_names(include_system_collections=False)
 
        collectionAlreadyAvailable = False
        for jj in previous_collections :

            if collName == jj :
                collectionAlreadyAvailable = True
                print(previous_collections)
                db.drop_collection(jj)
                
                print('Previous Similar collection found. Deleting it to avoid conflicts. Time : '+str(time))
                
                print('\n')
        if collectionAlreadyAvailable == False :
            print(previous_collections)
            print('No previous collections found. All Good!')

        x = coll.insert_many(objArr)
        print('\nAdded to database. Name : '+collName)
        print('\ncollections available \n')
        print(previous_collections)



