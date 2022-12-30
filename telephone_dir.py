from dotenv import load_dotenv, find_dotenv
import os
from pprint import pprint
import json
from pymongo import MongoClient,errors
from bson.objectid import ObjectId

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://Srinivas:{password}@freecluster.yrhda.mongodb.net/test"
client = MongoClient(connection_string)

mydb = client['Telephone_Directory'] 
# print(mydb.list_collection_names())
mycol = mydb['Customer_data']


'''Creating a single document'''


def insert_test_doc():
    collection =mydb['Customer_data']
    test_document = {
        "Name": "Vihaan",
        "Phone number": "89563214569",
        "Street":  "Shop No.6/6, Vihar Darshan, 7th Road, Vidyavihar(e), Ghatkoper (east)",
        "City" : "Mumbai",
        "State/province/area" :    "Maharashtra"
    }
    inserted_id = mycol.insert_one(test_document).inserted_id
    print(inserted_id)

# insert_test_doc()


'''creating multiple document and inserting it'''


def create_documents():
    Names = ["Minnie Van Ryder", "Ginger Plant","Rod Knee", "Karen Onnabit","Col Fays", "Anne Teak", "Art Decco"]
    Street = ["Rangwala Building 1st Floor, Islampura Street, Girgaum"," 5, 126, Gordhandas Bldg, Girgaon Rd, Girgaon" ,"113, Golden Chambers, New Link Rd, Opp Fame Adlab, Andheri (w)", " C 14 Sector 1","333, Sat Tad Kadim Masjid, Narshi Natha Street, Chinch Bunder", "Rangwala Building 1st Floor, Islampura Street, Girgaum", "Rangwala Building 1st Floor, Islampura Street, Girgaum"]
    Phone_number = ["02223079138","02225706432","231456635","56321563","0231230220","0221459862",'023123256']
    City = ["Mumbai","Mumbai","Mumbai","Mumbai","Mumbai","Mumbai","Mumbai"]
    State_province_area = ["Maharashtra","Maharashtra","Maharashtra","Maharashtra",'Maharashtra',"Maharashtra","Maharashtra"]

    docs = []

    for Names, Street, Phone_number,City,State_province_area in zip(Names, Street, Phone_number,City,State_province_area):
        doc = {"Names": Names, "Street":Street, "Phone_number":Phone_number,"City":City,"State_province_area":State_province_area}
        docs.append(doc) 
    seen = set()
    result = []
    for dic in docs:
        key = (dic['Names'])
        if key in seen:
            continue
        result.append(dic)
        seen.add(key)
    mycol.insert_many(result)

# create_documents()

'''TO find the records'''
def find_records():
    find_latest = mycol.find()
    for x in find_latest:
        print(x)


''' Update Document '''
def Update_Document():
    myquery = {"_id":ObjectId('63ae8f24f27e9766687fa74f')}
    newvalues = {"$set":{"City":"Visakhapatnam"}}
    mycol.update_one(myquery, newvalues)
    #print "customers" after the update:
    for x in mycol.find():
      print(x)

'''delete document'''
def delete_document():
    mycol.remove({'Names': 'Art Decco'})
    for x in mycol.find():
        print(x)