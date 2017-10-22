import httplib

def light_on():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
                
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/light/1")
    r1 = conn.getresponse()
    print r1.read()

def light_off():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/light/0")
    r1 = conn.getresponse()
    print r1.read()

def light_check():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/light/check/1")
    r1 = conn.getresponse()
    print r1.read()

def fan_on():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/fan/1")
    r1 = conn.getresponse()
    print r1.read()

def fan_off():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/fan/0")
    r1 = conn.getresponse()
    print r1.read()

def fan_check():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/fan/check/1")
    r1 = conn.getresponse()
    print r1.read()

def autolight_on():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part2_IP'])
    conn.request("GET", "/photocell/0")
    r1 = conn.getresponse()
    print r1.read()
    
def autolight_off():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part2_IP'])
    conn.request("GET", "/photocell/1")
    r1 = conn.getresponse()
    print r1.read()

def autolight_check():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part2_IP'])
    conn.request("GET", "/photocell/data")
    r1 = conn.getresponse()
    r2= r1.read().split(",")[1]

    if int(r2)==1:
        print "Room is dark"
    elif int(r2)==0:
        print "Room is not dark"

def temp_check():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/temp/check/1")
    r1 = conn.getresponse()
    print r1.read()

def humid_check():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/humid/check/1")
    r1 = conn.getresponse()
    print r1.read()

def pir_on():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/pir/1")
    r1 = conn.getresponse()
    print r1.read()

def pir_off():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/pir/0")
    r1 = conn.getresponse()
    print r1.read()

def pir_check():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/pir/check/1")
    r1 = conn.getresponse()
    print r1.read()

def smoke_off():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/smoke/0")
    r1 = conn.getresponse()
    print r1.read()
    
def smoke_on():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/smoke/1")
    r1 = conn.getresponse()
    print r1.read()

def smoke_check():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/smoke/check/1")
    r1 = conn.getresponse()
    print r1.read()

def door_lock():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part2_IP'])
    conn.request("GET", "/door/0")
    r1 = conn.getresponse()
    print r1.read()
    
def door_unlock():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part2_IP'])
    conn.request("GET", "/door/1")
    r1 = conn.getresponse()
    print r1.read()

def door_check():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part2_IP'])
    conn.request("GET", "/door/check/1")
    r1 = conn.getresponse()
    print r1.read()

def vibration_off():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part2_IP'])
    conn.request("GET", "/vibration/0")
    r1 = conn.getresponse()
    print r1.read()
    
def vibration_on():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part2_IP'])
    conn.request("GET", "/vibration/1")
    r1 = conn.getresponse()
    print r1.read()

def vibration_check():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part2_IP'])
    conn.request("GET", "/vibration/check/1")
    r1 = conn.getresponse()
    print r1.read()

def window_check():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part2_IP'])
    conn.request("GET", "/window/check/1")
    r1 = conn.getresponse()
    print r1.read()

def notification():
    dataList={}

    with open("../log/log") as log:
        for line in log:
            if line!="":
                value=line.split("=")[1].split('\n')[0].split("'")[1]
                key=line.split("=")[0]
                dataList[key]=value
    
    for key, value in dataList.iteritems():
        if value=="7":
            seg=key.split('_')[0]
            
    conn = httplib.HTTPConnection(dataList[seg+'_part1_IP'])
    conn.request("GET", "/notification")
    r1 = conn.getresponse()
    response1=r1.read()

    conn = httplib.HTTPConnection(dataList[seg+'_part2_IP'])
    conn.request("GET", "/notification")
    r1 = conn.getresponse()
    response2= r1.read()

    response=response1+"&"+response2
    
    print response
    
