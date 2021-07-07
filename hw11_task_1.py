import json
with open('dz.json','r',encoding='utf_8') as f:
    data = json.load(f)
    print(data)
    a = 0
    for i in data:
        #print(len(i['languages']))
        if len(i['languages'])>a:
            a = len(i['languages'])
            b = i['name']
    print(b)

