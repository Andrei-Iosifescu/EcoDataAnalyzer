import csv
stn=[]
lat=[]
long=[]
prov=[]
tm1=[]
tm2=[]
tm3=[]
tm4=[]
tm5=[]
tm6=[]
pre1=[]
pre2=[]
pre3=[]
pre4=[]
pre5=[]
pre6=[]
keep = 0
keepe = 0
keeper = 0
k = 0
kk = 0
kkk = 0
with open('example6.csv') as file1:
    rfile1 = csv.reader(file1,delimiter=',')
    count=0
    while count <32:
        next(rfile1)
        count = count + 1
    for row in rfile1:
        keep=keep+1
        stns=row[0]
        stn.append(stns)
        lats=row[1]
        lat.append(lats)
        longs=row[2]
        long.append(longs)
        provs=row[3]
        prov.append(provs)
        if row[4][:1]!="":
            tm1s=row[4]
            tm1.append(tm1s)
        else:
            tm1s="NA"
            tm1.append(tm1s)
        if row[14][:1]!="":
            pre1s=row[14]
            pre1.append(pre1s)
        else:
            pre1s="NA"
            pre1.append(pre1s)

with open('example1.csv') as file2:
    rfile2 = csv.reader(file2,delimiter=',')
    countm=0
    while countm <32:
        next(rfile2)
        countm = countm + 1
    for row in rfile2:
        keepe = keepe + 1
        if row[4][:1]!="":
            tm2s=row[4]
            tm2.append(tm2s)
        else:
            tm2s="NA"
            tm2.append(tm2s)
        if row[14][:1]!="":
            pre2s=row[14]
            pre2.append(pre2s)
        else:
            pre2s="NA"
            pre2.append(pre2s)
with open('example2.csv') as file3:
    rfile3 = csv.reader(file3, delimiter=',')
    countme=0
    while countme <32:
        next(rfile3)
        countme = countme + 1
    for row in rfile3:
        keeper = keeper + 1
        if row[4][:1]!="":
            tm3s=row[4]
            tm3.append(tm3s)
        else:
            tm3s="NA"
            tm3.append(tm3s)
        if row[14][:1]!="":
            pre3s=row[14]
            pre3.append(pre3s)
        else:
            pre3s="NA"
            pre3.append(pre3s)
with open('example3.csv') as file4:
    rfile4 = csv.reader(file4,delimiter=',')
    countmeu=0
    while countmeu <32:
        next(rfile4)
        countmeu = countmeu + 1
    for row in rfile4:
        k = k + 1
        if row[4][:1]!="":
            tm4s=row[4]
            tm4.append(tm4s)
        else:
            tm4s="NA"
            tm4.append(tm4s)
        if row[14][:1]!="":
            pre4s=row[14]
            pre4.append(pre4s)
        else:
            pre4s="NA"
            pre4.append(pre4s)
with open('example4.csv') as file5:
    rfile5 = csv.reader(file5,delimiter=',')
    countmeup=0
    while countmeup <32:
        next(rfile5)
        countmeup = countmeup + 1
    for row in rfile5:
        kk = kk + 1
        if row[4][:1]!="":
            tm5s=row[4]
            tm5.append(tm5s)
        else:
            tm5s="NA"
            tm5.append(tm5s)
        if row[14][:1]!="":
            pre5s=row[14]
            pre5.append(pre5s)
        else:
            pre5s="NA"
            pre5.append(pre5s)
with open('example5.csv') as file6:
    rfile6 = csv.reader(file6,delimiter=',')
    countmeups=0
    while countmeups <32:
        next(rfile6)
        countmeups = countmeups + 1
    for row in rfile6:
        kkk = kkk + 1
        if row[4][:1]!="":
            tm6s=row[4]
            tm6.append(tm6s)
        else:
            tm6s="NA"
            tm6.append(tm6s)
        if row[14][:1]!="":
            pre6s=row[14]
            pre6.append(pre6s)
        else:
            pre6s="NA"
            pre6.append(pre6s)
counter = 0
with open('result.csv', 'wb') as result:
    filewriter=csv.writer(result,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["Stn_Name", "Lat", "Long", "Prov","TM","P"])
    listy=[keep,keepe,keeper,k,kk,kkk,]
    winner=min(listy)
    while counter < winner:
        tmsum = 0
        tmsums=0
        avcount = 0
        avcounts= 0
        name = stn[counter]
        latitude = lat[counter]
        longitude = long[counter]
        province = prov[counter]
        if tm1[counter]!="NA":
            avcount=avcount+1
            dd=float(tm1[counter])
            dd=round(dd,2)
            tmsum=tmsum+dd
        if tm2[counter]!="NA":
            avcount=avcount+1
            d = float(tm2[counter])
            d = round(d, 2)
            tmsum = tmsum + d
        if tm3[counter] != "NA":
            avcount = avcount + 1
            ddd = float(tm3[counter])
            ddd = round(ddd, 2)
            tmsum = tmsum + ddd
        if tm4[counter] != "NA":
            avcount = avcount + 1
            dddd = float(tm4[counter])
            dddd = round(dddd, 2)
            tmsum = tmsum + dddd
        if tm5[counter] != "NA":
            avcount = avcount + 1
            ddddd = float(tm5[counter])
            ddddd = round(ddddd, 2)
            tmsum = tmsum + ddddd
        if tm6[counter] != "NA":
            avcount = avcount + 1
            dddddd = float(tm6[counter])
            dddddd = round(dddddd, 2)
            tmsum = tmsum + dddddd
        if pre1[counter]!="NA":
            avcounts=avcounts+1
            a = float(pre1[counter])
            a = round(a, 2)
            tmsums = tmsums + a
        if pre2[counter]!="NA":
            avcounts=avcounts+1
            aa = float(pre2[counter])
            aa = round(aa, 2)
            tmsums = tmsums + aa
        if pre3[counter]!="NA":
            avcounts=avcounts+1
            aaa = float(pre3[counter])
            aaa = round(aaa, 2)
            tmsums = tmsums + aaa
        if pre4[counter]!="NA":
            avcounts=avcounts+1
            aaaa = float(pre4[counter])
            aaaa = round(aaaa, 2)
            tmsums = tmsums + aaaa
        if pre5[counter]!="NA":
            avcounts=avcounts+1
            aaaaa = float(pre5[counter])
            aaaaa = round(aaaaa, 2)
            tmsums = tmsums + aaaaa
        if pre6[counter]!="NA":
            avcounts=avcounts+1
            aaaaaa = float(pre6[counter])
            aaaaaa = round(aaaaaa, 2)
            tmsums = tmsums + aaaaaa
        if tm1[counter]=="NA" and tm2[counter]=="NA" and tm3[counter]=="NA" and tm4[counter]=="NA" and tm5[counter]=="NA" and tm6[counter]=="NA":
            tmthings="NA"
        else:
            taverage=tmsum/avcount
            taverage=round(taverage,2)
            tmthings=taverage
        if pre1[counter] == "NA" and pre2[counter] == "NA" and pre3[counter] == "NA" and pre4[counter] == "NA" and pre5[counter] == "NA" and pre6[counter] == "NA":
            prethings = "NA"
        else:
            taverages = tmsums / avcounts
            taverages = round(taverages, 2)
            prethings = taverages
        filewriter.writerow([name, latitude, longitude, province, tmthings, prethings])
        counter=counter+1
#comment