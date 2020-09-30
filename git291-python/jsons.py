import json

j = {
  "emp": [
    {"name": "Fukui"},
    {"name": "Yoshiharu"}
  ]
}



with open('test.json', 'w') as f:
  json.dump(j, f)
with open('test.json', 'r') as f:
  print(json.load(f))

js = json.dumps(j)
print(type(json.loads(js)))