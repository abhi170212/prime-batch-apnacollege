import json 

# json.dump() , json.load() and json.loads(),json.dumps()
#module shadowing problem happened here -> modules ke naam apr file ka naam nhi hona chhaiye 
json_str = '{"name":"Abhishek" , "isTeacher":false}'
py_obj = json.loads(json_str)
print(type(json_str))
print(py_obj)


py_dict = {
     "city":"London",
     "club":{
          "east":"Arsenal",
          "west":"Chelsea",
          "central":"Tottenham",
          "North_east":"Aston Villa"
     },
     "league":"English Premier league",
     "is_good":False
}
json_obj = json.dumps(py_dict)
print(json_obj)



