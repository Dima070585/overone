import json
with open('dz.json','r',encoding='utf_8') as f:
    data = json.load(f)
    print(data)
    a = 0
    b = 0
    k = 0
    rez = 0
    for i in data:
        a = int(i['birthday'][6:])
        if a < 2000:
            print(i['name'])
            b += i['height']
            k += 1
    rez = b/k
    print(rez)
