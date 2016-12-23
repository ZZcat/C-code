import os
folder = os.popen("pwd").readlines()

import urllib2

def internet_on():
    try:
        urllib2.urlopen('https://github.com/ZZcat/', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

if internet_on:
    print "Connected to server"
    folder = str(folder)
    print "Loading folder..."
    folder,trash = folder.split("C-code")
    trash,folder = folder.split("'")

    print "Removing old directory..."
    com = "(cd '"+str(folder)+"'&&rm -rf C-code)"
    os.system(com)
    print "Updating..."
    com = '(cd "'+str(folder)+'"&&git clone https://github.com/ZZcat/C-code.git)'
    os.system(com)
    print com
    
    print "Enabling bash"
    com = '(cd "'+str(folder)+'C-code/"&&chmod -x r.bash)'   "hmod -x r.bash "
    
    print "Running program"
    com = '(cd "'+str(folder)+'C-code/"&&./r.bash)'
    print com
    os.system(com)
    
else:
    print "Unable to connect to ZZcat's github profile"
    print "Running program in offline mode"
