#vahid.zahani@gmail.com
#this is edit in drpbox mobile
import subprocess
import urllib.request
import time,json

def getIp():
    data=urllib.request.urlopen("https://api.projfa.ir/ip").read().decode('utf-8')
    data=json.loads(data)
    return(data['ip'])

lastip="NOIP"
while True:
    try:
        newip=getIp()
        if (lastip!=newip):
            # with open("d:\\aaa.txt", "w") as f:
            #     f.write(lastip +" -> "+ newip +' IP Change!\n')
            #subprocess.Popen('notepad "d:\\aaa.txt"')
            lastip=newip
            print("changed IP")
        print(newip)
    except :
        print("Error to connect")
    time.sleep(4)




    
