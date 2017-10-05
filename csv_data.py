import csv
import re
import sys    
data = []
file1=sys.argv[1]
replaced=[]
with open(file1) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        data.append(row[6])
    i = 1
    while i < len(data):
        
        data[i]=data[i].replace("Standard query ","")
        data[i]=data[i].replace("response ","")
        data[i]=data[i].replace("CNAME ","")
        data[i] = data[i][:0] + data[i][6:]
        #print(data[i])
        i += 1
    #print(data)
    i = 1
    k=0
    Subdomain=[]
    IpV = []
    while i < len(data):
        store = []
        store=data[i].split( )
        j=0
        flag=0
        while j<len(store):
            if(store[j]=="A"):
                flag=0
                j+=1
                continue
            elif(store[j]=="AAAA"):
                flag=1
                j+=1
                continue
            else:
                if(flag==0):
                    IpV.append("A")
                else:
                    IpV.append("AAAA")
                Subdomain.append(store[j])
                print(Subdomain[k])
                
                k+=1
                j+=1
        i += 1
with open('output.csv', 'w') as csvfile:
    fieldnames = ['Ip_Version', 'Subdomain']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    i=0
    writer.writeheader()
    while i<len(IpV):
        writer.writerow({'Ip_Version': IpV[i], 'Subdomain': Subdomain[i]})
        i+=1
#with open('outcome.csv', 'w') as csvfile:
#    g = csv.writer(csvfile)
#    j=0
#    while j<len(IpV):
#        if(j==0):
#            g.writerows('IP Version','Subdomain')
#        g.writerow(IpV[j])
#        j+=1