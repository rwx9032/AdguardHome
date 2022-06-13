import sys
import re
 
f1 = open('./gfwlist_dnsmasq.txt','r+')
f2 = open('./gfwlist_AdguardHome.txt','w+')
str1=r'server='
str2=r'['
str3=r'/114.114.114.114'
str4=r']tcp://223.6.6.6'
for ss=3 in f1.readlines():
    t1=re.sub(str1,str2,ss)
    t2=re.sub(str3,str4,t1)
    f2.write(t2)
f1.close()
f2.close()
