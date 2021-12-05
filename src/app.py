import json

x = {
"Name" : "Thorfinn" ,
"Age" : 15 ,
"Weapon" : "2 Daggers" 
}

y = json.dumps(x)

print(y)