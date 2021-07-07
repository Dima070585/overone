
from datetime import timedelta
from datetime import datetime
#from datetime import strptime
#from itertools import
#from datetime import strptime
table=[]

while True:
    print("")
    choice = int(input("введите число от 1 до 4: "))
    if choice == 1:
        info = {'Number':input(),'Arival point':input(),'Arival time':
        datetime.strptime(input('введите d/m/y h:r'),'%d/%m/%y %H:%M'),'Distation':input(),
        'Dep.time':datetime.strptime(input('введите d/m/y h:r'),'%d/%m/%y %H:%M')}
        info['Time in trip']=info['Dep.time'] - info['Arival time']
        table.append(info)
    elif choice == 2:
        for i in table:
            print(i)
    elif choice == 3:
        for i in table:
            if i['Time in trip']>=timedelta(hours=7,minutes=20):
                print(i)



    elif choice == 4:
        break



