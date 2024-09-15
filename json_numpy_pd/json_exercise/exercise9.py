# Parse the following JSON to get all the values of a key ‘name’ within an array
import json 


def get_name(some_array):
    for dict in some_array:
        print(dict.get('name'))

arrayJson = '''[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]'''

array = json.loads(arrayJson)
get_name(array)