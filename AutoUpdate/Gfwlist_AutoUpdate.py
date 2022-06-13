import sys
import re
 
f1 = open('./gfwlist_dnsmasq.conf','r+')
f2 = open('./gfwlist_AdguardHome.txt','w+')
str1=r'server='
str2=r'['
str3=r'/127.0.0.1#5353'
str4=r']tls://1.1.1.1'
for ss in f1.readlines():
    t1=re.sub(str1,str2,ss)
    t2=re.sub(str3,str4,t1)
    f2.write(t2)
f1.close()
f2.close()
