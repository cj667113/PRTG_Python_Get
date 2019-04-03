import requests
import json
import re
import time
def prtg_collect():
    prtg_setup=['username','hashpass','sensorid'] #Username,#Passhash,#SensorID
    url = "https://monitor.its.ohio.edu/api/table.json?noraw=1&content=channels&sortby=name&columns=name=textraw,minimum,maximum,condition,lastvalue&id=%s&login=%s&passhash=%s" %(prtg_setup[2],prtg_setup[0],prtg_setup[1])
    data_raw = requests.get(url=url)
    data=(json.loads(data_raw.text))
    data=str(data)
    data=re.split("\{|}|\[|]",data)
    options=[''"u'lastvalue': " '' , ''" u'name': " ''] ##Used split along lastvalue and channel names
    search_parm=['var#1','var#2'] ##Specify what channel names to split/channel names needed to be returned
    search_parm_2=[''"u'var#1'"'',''"u'var#2'"''] ##Specific unicode pattern to return of channel names
    gather=[]
    format=[]
    for item in data:
        if len(item)>=1:
            item=item.split(",")
            for x in item:
                if re.search(options[0],x):
                    if len(x)>17:
                        z=x.split(options[0])
                        for y in z:
                            if len(y)>0:
                                gather.append((y))      
                for y in search_parm:
                    if re.search(y,x):
                        if len(x)>17:
                            z=x.split(options[1])
                            for y in z:
                                if len(y)>0:
                                    gather.append((y))
    for x in gather:
        for y in search_parm_2:
            if x==y:
                format.append((x,gather[(gather.index(x))-1]))
    print(format)
while True:
    prtg_collect()
    time.sleep(1)
