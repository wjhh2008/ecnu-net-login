import os
import urllib
import ConfigParser
import urllib2
import getinfo
url = 'http://10.255.44.33/cgi-bin/srun_portal'


cf = ConfigParser.ConfigParser()
cf.read("config.ini")


username = cf.get("info","username")

password = cf.get("info","password")
do_login = {'action':'login',
          'username':username,
          'password':password,
          'ac_id':'6',
          'type':'1',
          'wbaredirect':'',
          'mac':'',
          'user_ip':''
         }
do_logout = {'action':'login'
         }
data = urllib.urlencode(do_login)
#print data
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()


if the_page.find("login_ok"):
    print "Successful login !"
    getinfo.doit()

else:
    print the_page
    
os.system("pause")
