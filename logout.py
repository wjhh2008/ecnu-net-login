import os
import urllib
import urllib2
import getinfo
getinfo.doit()
url = 'http://10.255.44.33/cgi-bin/srun_portal'
urlinfo = 'http://10.255.44.33/cgi-bin/rad_user_info'
do_logout = {'action':'logout'
         }
data = urllib.urlencode(do_logout)
#print data
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page.decode("UTF-8")
os.system("pause")




