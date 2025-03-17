#Yola bağlı olarak cisimlerin ivmelerine göre yaptıkları işi fiziksel olarak hesaplayan Python kodu

import math

kutle=[12,23,43,45,14,90]
a=int(input("Cisimlerin sabit ivmesi nedir? "))
kuvvet=[]
for m in range(len(kutle)):
    f = kutle[m]*a
    kuvvet.append(f)
    m+=1
print("Hesaplanan tüm kuvvetler: ",kuvvet)

x=int(input("Yolun uzunluğu nedir? "))
s=int(input("Sürtünme kuvveti kaç? "))
a=int(input("Kaç derecelik bir açı var? "))
net_iş=[]
i=0
v=0
while True:
    if i <= len(kuvvet)-1:
        net= (kuvvet[i]*x*math.cos(math.radians(a))) - (s*x)
        net_iş.append(net)
        i+=1
    else:
        break
    while v <= len(kuvvet)-1:
        print("Kuvvet: " , kuvvet[v] , " olduğunda " , "yapılan Net_Is: " , net_iş[v] , " olur.")
        v+=1
        break
    