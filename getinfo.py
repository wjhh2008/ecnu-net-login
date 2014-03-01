import os
import urllib2
def doit():
    urlinfo = 'http://10.255.44.33/cgi-bin/rad_user_info'
    req = urllib2.Request(urlinfo, "")
    response = urllib2.urlopen(req)
    the_page = response.read()
    if the_page=="not_online":
        print "Please login"
    else:
        u=the_page.split(",")
        print "Used:  "+str(int(u[6])/1024/1024)+"MB"

if __name__  == "__main__": 
    doit()
    os.system("pause")
