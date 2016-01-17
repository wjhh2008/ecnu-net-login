import os
import time
import urllib
import ConfigParser
import urllib2
import getinfo
import sys
url = 'http://10.9.27.18/include/auth_action.php'


cf = ConfigParser.ConfigParser()
cf.read(sys.path[0]+"/config.ini")
print sys.path[0]

username = cf.get("info","username")

password = cf.get("info","password")
do_login = {'action':'login',
          'username':username,
          'password':password,
          'ac_id':'4',
          'user_ip':'',
          'nas_ip':'',
          'user_mac':'',
          'save_me':'0',
          'ajax':'1'
         }
do_logout = {'action':'login'
         }
data = urllib.urlencode(do_login)
status = False
while True:
    ret = os.system('ping -c 2 114.114.114.114 >/dev/null')
    if ret:
        status = False
        try:
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            the_page = response.read()
        except:
            pass
        print 'try connecting ...'
    else:
        if status==False:
            status = True
            print 'connected'
    time.sleep(10)

#print the_page
#if the_page.find("login_ok"):
#    print "Successful login !"
#    getinfo.doit()

#else:
#    print the_page    
#os.system("pause")
