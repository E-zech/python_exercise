# Access the nested key ‘salary’ from the following JSON
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

py_dict = json.loads(sampleJson)
print(py_dict["company"]["employee"]["payble"]["salary"])