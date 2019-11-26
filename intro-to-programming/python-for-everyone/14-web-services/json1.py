import json

data = """
{
    "name" : "Chuck",
    "phone" : {
        "type": "intl",
        "number" : "+1 734 303 4456"
    },
    "email":{
        "hide" : "yes"
    }
}
"""

info = json.loads(data)
print("Name: {}".format(info["name"]))
print("Hide: {}".format(info["email"]["hide"]))


