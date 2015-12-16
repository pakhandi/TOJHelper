#TIMUS ONLINE JUDGE
import mechanize
import re
import os
import shutil
from bs4 import BeautifulSoup
#print "Enter question no."
qno=raw_input();
#qno=sys.argv[1]
myurl="http://acm.timus.ru/problem.aspx?num="+qno

br=mechanize.Browser()

prx = open("proxy",'r')
prx_set = prx.readline()
prx_set = prx_set.split('\n',1)
prx_set = prx_set[0]

#Format:br.set_proxies({"http":"username:password@proxy:port"})
if(len(prx_set)!=0):
    print prx_set
    br.set_proxies({"http":prx_set})

br.set_handle_robots(False)

response=br.open(myurl)
print response.code

br.addheaders=[('User-agent','Firefox')]

response=br.open(myurl)
#print response.read()

soup=BeautifulSoup(response)

for tbl in soup.findAll('table','sample'):
    if (os.path.exists(qno)):
        print "Folder Exists"
    else:
        os.makedirs(qno)  

    shutil.copyfile("template.cpp", qno+"/"+qno+".cpp" )    

    detach_dir=qno+"/"
    incounter=1
   
    for item in tbl.findAll('pre','intable'):
        if incounter%2 == 1:
            att_path=os.path.join(detach_dir,"in"+str((incounter/2))+".txt")
            print att_path
            fo=open(att_path,'wb')
        else:
            att_path=os.path.join(detach_dir,"out"+str((incounter/2)-1)+".txt")
            print att_path
            fo=open(att_path,'wb')
        incounter+=1
        item=str(item).replace("<pre class=\"intable\">","")
        item=str(item).replace("</pre>","")
        item=str(item).replace("<br/>","\n")
        fo.write(item)

