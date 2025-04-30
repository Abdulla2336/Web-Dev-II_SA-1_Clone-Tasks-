import json
with open("data.json","r") as file :
    info= json.load(file)

print (info["drinks"][0]["idDrink"])
print (info["drinks"][1]["strDrink"])
