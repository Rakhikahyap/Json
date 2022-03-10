import json
b={'4':5,'6':7,'1':3,'2':4}
py_ob=dict(sorted(b.items()))
json_ob=json.dumps(py_ob,indent=6)
print(json_ob)






