import  json
# json_ob='{"name":"rakhi","clas":"B.A.","Age":"19"}'
# py_ob=json.loads(json_ob)
# print(py_ob,type(py_ob))

# py_ob={"name":"rakhi","clas":"B.A.","Age":"19"}
# json_ob=json.dumps(py_ob,indent=6)
# print(json_ob,type(json_ob))

py_ob={"name":"David","class":"I","age":6}
json_ob=json.dumps(py_ob,indent=6)
print(json_ob,type(json_ob))

     